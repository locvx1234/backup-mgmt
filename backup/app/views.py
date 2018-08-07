import sys
import os
import re
import fileinput
import datetime
import json
import logging

from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.views import PasswordResetView as BasePasswordResetView, SuccessURLAllowedHostsMixin
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME, get_user_model
from django.shortcuts import get_object_or_404, resolve_url
from django.utils.http import is_safe_url
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

import yaml
import netifaces
import pytz
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet

from .models import Computer, Sync, Schedule
from django.views import generic
from ipaddress import ip_address
from django.shortcuts import redirect
from django.urls import reverse_lazy
from pprint import pprint
from django.forms.models import model_to_dict
from app import cores


logger = logging.getLogger(__name__)


def get_agent_info(agent_id):
    agent = Computer.objects.all().filter(id=agent_id)[0]
    agent_info = Computer.objects.filter(id=agent_id).values()[0]
    used_data = 0
    syncs = agent.sync_set.all()

    if len(syncs) >= 1:
        agent_info['all_sync'] = syncs
        last_sync = syncs[0]
        for sync in syncs:
            used_data += sync.amount_data_change
        agent_info['used_data'] = used_data
    else:
        last_sync = None
    if last_sync:
        agent_info['last_sync'] = last_sync.sync_time
    return agent_info


def get_all_interface():
    interfaces = []
    list_interface = netifaces.interfaces()
    for interface in list_interface:
        dict_interface = {}
        if is_interface_up(interface):
            dict_interface['iface'] = interface
            dict_interface['state'] = "UP"
            dict_interface['ip'] = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        else:
            dict_interface['iface'] = interface
            dict_interface['state'] = "DOWN"
            dict_interface['ip'] = 'Disable'
        interfaces.append(dict_interface)
    return interfaces


def agent_used_data():
    pass


def index(request):
    if request.user.is_authenticated:
        pass
    else:
        return HttpResponseRedirect('/login')

    context = {}
    # find a public IP, if cant get a private instead
    interfaces = [x for x in get_all_interface() if x['ip'] != 'Disable']
    private_ip = None
    public_ip = None
    for interface in interfaces:
        if ip_address(interface['ip']).is_global:
            public_ip = interface['ip']
        elif not private_ip and not ip_address(interface['ip']).is_loopback:
            private_ip = interface['ip']
    if not public_ip:
        context['ip'] = private_ip
        context['ip_type'] = 'private'
    else:
        context['ip'] = public_ip
        context['ip_type'] = 'public'

    # get all computer and disk used with each computer
    all_computer = Computer.objects.all()
    context['agents'] = all_computer
    disk_used_obs = []
    last_sync_obs = []
    total_protect_data = 0
    for computer in all_computer:
        syncs_of_computer = computer.sync_set.all()
        if syncs_of_computer:
            last_sync = syncs_of_computer[0]
        else:
            last_sync = None
        used_disk = 0
        for sync in syncs_of_computer:
            used_disk += sync.amount_data_change
        disk_used_obs.append({'name': computer.name, 'used_disk': used_disk})
        last_sync_obs.append({'name': computer.name, 'last_sync_time': last_sync.sync_time if last_sync else None})

    context['agents_count'] = len(context['agents'])
    context['disk_used'] = disk_used_obs
    context['last_syncs'] = last_sync_obs
    for disk_used_ob in disk_used_obs:
        total_protect_data += disk_used_ob['used_disk']

    context['total_protect_data'] = total_protect_data

    context['ip_offsite'] = settings.OFFSITE_SERVER
    context['speed_limit'] = settings.OFFSITE_LIMIT_SPEED
    return render(request, 'app/index.html', context)


def reboot():
    os.system('reboot')
    return


def device_setting(request):
    # get servers list 
    servers_list = settings.CORE_DOMAIN
    servers_list = ', '.join(servers_list)
    print(servers_list)
    # get timezone
    timezone = settings.TIME_ZONE
    list_timezone = pytz.all_timezones

    # get time to refresh page
    with open("app/templates/app/base_site.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    meta_refresh = soup.findAll(attrs={"http-equiv": "refresh"})
    time_refresh = str(meta_refresh[0]['content'])

    if request.method == 'POST':
        # change CORE_DOMAIN in settings.py
        if request.POST.get('add_server'):
            servers = request.POST.get('add_server')
            servers = str([x.strip() for x in servers.split(',')])
            for line in fileinput.input(settings.BASE_DIR + '/backup/settings.py', inplace=True):
                if line.strip().startswith('CORE_DOMAIN = '):
                    line = 'CORE_DOMAIN = ' + servers + "\n"
                sys.stdout.write(line)

        # change TIME_ZONE in settings.py
        if request.POST.get('timezone-select'):
            timezone = request.POST.get('timezone-select')
            for line in fileinput.input(settings.BASE_DIR + '/backup/settings.py', inplace=True):
                if line.strip().startswith('TIME_ZONE = '):
                    line = 'TIME_ZONE = ' + "'" + timezone + "'\n"
                sys.stdout.write(line)

        if request.POST.get('refresh-select'):
            time_refresh = request.POST.get('refresh-select')
            meta_refresh[0]['content'] = time_refresh
            with open("app/templates/app/base_site.html", "w") as outf:
                outf.write(str(soup))

    return render(request, 'app/device_setting.html', {'servers_list': servers_list, 'timezone': timezone,
                                                       'list_tz': list_timezone, 'time_refresh': time_refresh})


def networking(request):
    interfaces = []
    list_interface = netifaces.interfaces()
    for interface in list_interface:
        dict_interface = {}
        if is_interface_up(interface):
            dict_interface['iface'] = interface
            dict_interface['state'] = "UP"
            dict_interface['ip'] = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        else:
            dict_interface['iface'] = interface
            dict_interface['state'] = "DOWN"
            dict_interface['ip'] = 'Disable'

        interfaces.append(dict_interface)
    dns = []
    if request.method == 'POST':

        dns1 = request.POST.get('dns1')
        dns2 = request.POST.get('dns2')
        dns3 = request.POST.get('dns3')
        search_domain = request.POST.get('dns-search')
        for i in range(1,4):
            if eval('dns' + str(i)):
                cmd = "sed -i '"+ str(i) + "s/.*/nameserver " + eval('dns' + str(i)) + "/' /etc/resolv.conf"
                os.system(cmd)

        if search_domain:
            cmd = "sed -i 's/search .*/search " + search_domain + "/' /etc/resolv.conf"
            os.system(cmd)
    dns = get_resolvers()
    print(dns)
    return render(request, 'app/networking.html', {'interfaces': interfaces, 'dns': dns})


def get_resolvers():
    resolvers = []
    dns = {}
    try:
        with open( '/etc/resolv.conf', 'r' ) as resolvconf:
            for line in resolvconf.readlines():
                line = line.split('#', 1)[0]
                line = line.rstrip()
                if 'nameserver' in line:
                    resolvers.append(line.split()[1])
                if 'search' in line:
                    dns['search'] = line.split()[1]
            dns['resolver'] = resolvers
        return dns
    except IOError as error:
        return error.strerror


def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr


class UsersView(TemplateView):
    template_name = 'app/contact.html'

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context


def agent(request, agent_id=None):
    agents_info = []
    agents = Computer.objects.all()
    data_used = 0

    for agent in agents:
        agent_syncs = agent.sync_set.all()
        if agent_syncs:
            last_sync = agent_syncs[0]
        else:
            last_sync = None
        for sync in agent_syncs:
            data_used += sync.amount_data_change

        progressing_jobs = agent.schedule_set.filter(status=1)
        if progressing_jobs:
            progressing_points = progressing_jobs.values_list("path", flat=True)
        else:
            progressing_points = None

        agents_info.append({'agent': agent, 'data_used': data_used, 'last_sync_time': last_sync.sync_time if last_sync else None,
                            'progressing_points': progressing_points})
    if request.method == 'POST':
        if agent_id:  # start backup button
            computer = Computer.objects.get(id=agent_id)
            schedules = Schedule.objects.filter(computer=computer, status=2)
            for schedule in schedules:
                new_job = Schedule(time=timezone.now(), typeofbackup=0,
                                   ip_server=schedule.ip_server, computer=computer, path=schedule.path)
                new_job.save()
                logger.info("Force backup " + computer.name + " - " + schedule.path)
        else:  # add new agent
            username = request.POST.get('agent-username')
            name = request.POST.get('agent-name') or username

            # add user to core
            response = cores.add_agent(settings.CORE_DOMAIN[0], username)

            if response.status_code == 200:
                res_json = response.json()
                token = res_json['token']
                key = res_json['key']

                # add agent to manager site
                computer = Computer(username=username, name=name, token=token, key=key)
                computer.save()
                logger.info("Agent " + name + " created")
                return HttpResponseRedirect(reverse('agent'))

            elif response.status_code == 409:  # user existed
                msg = response.text
                logger.error(msg)
                return HttpResponseRedirect(reverse('agent'))

    return render(request, 'app/agent.html', {'agents': agents_info})


def delete_agent(request, agent_id):
    agent = Computer.objects.get(id=agent_id)

    # delete user in core
    response = cores.remove_agent(settings.CORE_DOMAIN[0], agent.username)

    if response.status_code == 200:
        # delete agent in manager site
        agent.delete()
        logger.info("Agent " + agent.name + " deleted")
        return HttpResponseRedirect('/agent')


def delete_sync(request, sync_id):
    sync = Sync.objects.filter(id=sync_id)
    sync.delete()
    logger.info("Sync: " + sync.computer.name + " - " +  str(sync.sync_time) + " deleted")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def recover_point(request, agent_id):
    context = {}
    agent = get_agent_info(agent_id)
    context['agent'] = agent
    return render(request, 'app/recovery_point.html', context)


def restore(request):
    agents = Computer.objects.all()

    return render(request, 'app/restore.html', {'agents': agents})


def next_day(dnow, d):
    if d.time() > dnow.time():
        return str(dnow.date()) + ' ' + str(d.time())
    else:
        dnext = dnow + datetime.timedelta(days=1)  # increase a day
        return str(dnext.date()) + ' ' + str(d.time())


def next_weekday(now, weekday, d):           
    days_ahead = weekday - now.weekday()    
    if days_ahead < 0 or ( days_ahead == 0 and d.time() < now.time() ):
        days_ahead += 7                                                                        
    return str((now + datetime.timedelta(days_ahead)).date()) + ' ' + str(d.time())


def config_agent(request, computer_id):
    context = {}
    computer = Computer.objects.get(id=computer_id)
    schedules = Schedule.objects.filter(computer=computer)

    if request.method == 'POST':
        path = request.POST.get('path')

        typeofbackup = request.POST.get('typeofbackup')
        ip_server = request.POST.get('server-backup')
        print(typeofbackup)

        if typeofbackup == '0':  # once
            time = request.POST.get('datetime')
            print(time)
            schedule = Schedule(time=time, typeofbackup=typeofbackup, 
                                ip_server=ip_server, computer=computer, path=path)
            schedule.save()

        elif typeofbackup == '1':  # daily
            daily_time = request.POST.get('time')
            d = datetime.datetime.strptime(daily_time, '%H:%M')
            dnow = datetime.datetime.now()
            time = next_day(dnow, d)

            schedule = Schedule(time=time, typeofbackup=typeofbackup,
                                ip_server=ip_server, computer=computer, path=path)
            schedule.save()

        elif typeofbackup == '2':  # weekly
            days = request.POST.getlist('dayofweek')
            dnow = datetime.datetime.now()
            dtime = request.POST.get('time')
            d = datetime.datetime.strptime(dtime, '%H:%M')
            for weekday in days:
                time = next_weekday(dnow, int(weekday), d)
                schedule = Schedule(time=time, typeofbackup=typeofbackup,
                                ip_server=ip_server, computer=computer, path=path)
                schedule.save()

        return HttpResponseRedirect(reverse('config-agent', kwargs={'computer_id': computer_id}))

    context = {'schedules': schedules, 'serverlist': settings.CORE_DOMAIN, 'computer': computer}
    return render(request, 'app/config_agent.html', context)


def delete_schedule(request, schedule_id):
    print(schedule_id)
    schedule = Schedule.objects.filter(id=schedule_id)
    schedule.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class Agent(generic.ListView):
    template_name = 'app/agent.html'
    context_object_name = 'agents'

    def get_queryset(self):
        return Computer.objects.all()


def contact(request):
    print('RECEIVED REQUEST: ' + request.method)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        organization = request.POST.get('organization')
        data_contact = dict(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            organization = organization,
        )
        with open(os.path.join(settings.MEDIA_ROOT, 'support_contact.yml'), 'w') as outfile:
            yaml.dump(data_contact, outfile, default_flow_style=False)

    with open(os.path.join(settings.MEDIA_ROOT, 'support_contact.yml'), 'r') as stream:
        data_loaded = yaml.load(stream)

    print(data_loaded)
    user_list = User.objects.all()
    print(user_list)
    return render(request, 'app/contact.html', {'data_contact': data_loaded, 'user_list': user_list})

# def error_404(request):
#         return render(request,'app/page_404.html', status=404)
#
# def error_500(request):
#         return render(request,'app/page_500.html', status=500)


def off_site_sync(request):
    now = datetime.datetime.now()
    date_now = now.date()
    week_now = date_now.isocalendar()[1]
    data_change = []
    all_computer = Computer.objects.all()
    ip_offsite = settings.OFFSITE_SERVER
    speed_limit = settings.OFFSITE_LIMIT_SPEED
    daily_total = 0
    weekly_total = 0
    for computer in all_computer:
        rate_change = {}
        rate_change['computer'] = computer.name
        syncs_of_computer = computer.sync_set.all()
        daily_change = 0
        weekly_change = 0

        for sync in syncs_of_computer:
            date_sync = sync.sync_time.date()
            week_sync = date_sync.isocalendar()[1]
            if date_sync == date_now:
                daily_change += sync.amount_data_change
            if week_sync == week_now:
                weekly_change += sync.amount_data_change
        print(daily_change)
        daily_total += daily_change
        weekly_total += weekly_change

        rate_change['daily'] = daily_change
        rate_change['weekly'] = weekly_change
        data_change.append(rate_change)

    if request.method == 'POST':
        if request.POST.get('ip_offsite'):
            ip_offsite = request.POST.get('ip_offsite')
            for line in fileinput.input(settings.BASE_DIR + '/backup/settings.py', inplace=True):
                if line.strip().startswith('OFFSITE_SERVER = '):
                    line = 'OFFSITE_SERVER = ' + "'" + ip_offsite + "'\n"
                sys.stdout.write(line)

        if request.POST.get('speed_limit'):
            speed_limit = request.POST.get('speed_limit')
            for line in fileinput.input(settings.BASE_DIR + '/backup/settings.py', inplace=True):
                if line.strip().startswith('OFFSITE_LIMIT_SPEED = '):
                    line = 'OFFSITE_LIMIT_SPEED = ' + "'" + speed_limit + "'\n"
                sys.stdout.write(line)

    return render(request, 'app/offsite-sync.html',
                  {'data_change': data_change, 'ip_offsite': ip_offsite, 'speed_limit': speed_limit,
                   'daily_total': daily_total, 'weekly_total': weekly_total})


# API
def get_header(request):
    regex = re.compile('^HTTP_')
    header = dict((regex.sub('', header), value) for (header, value)
                   in request.META.items() if header.startswith('HTTP_'))
    return header


def get_computer_by_token(request):
    header = get_header(request)
    try:
        token = header['AUTHORIZATION']
        computer = Computer.objects.get(token=token)
        return computer 
    except (KeyError, Computer.DoesNotExist):
        return None


def get_job(request):
    computer = get_computer_by_token(request)
    if computer:
        all_jobs = computer.schedule_set.values()
        now = timezone.now()
        list_jobs = []
        for job in all_jobs:
            if job['time'] < now and job['status'] == 2:
                list_jobs.append({"job_id": job['id'], "path": job['path'], "server": job['ip_server']})

                # mark job processing
                job = Schedule.objects.get(id=job['id'])
                job.status = 1
                job.save()

        data = {"jobs": list_jobs}

        cipher_suite = Fernet(computer.key)
        cipher_text = cipher_suite.encrypt(json.dumps(data).encode())
        return HttpResponse(cipher_text)
    else:
        return HttpResponse('Unauthorized', status=401)


@csrf_exempt
def handle_result(request):
    if request.method == 'POST':
        computer = get_computer_by_token(request)
        if computer:
            request_data = json.loads(request.body.decode())
            print(request_data)
            if request_data['status_code'] == 200:
                # New Sync record
                now = timezone.now()
                Sync.objects.create(computer=computer, amount_data_change=float(request_data["data_change"])/1024/1024, sync_time=now )
                
                if request_data['job_id'] == None:  # client manual backup
                    pass
                else:
                    # mark job complete
                    print("change status")
                    job = Schedule.objects.get(id=request_data['job_id'])
                    job.status = 0
                    job.save()
                    print("ok")

                    # extend job
                    print(job.typeofbackup)
                    if job.typeofbackup != 0:
                        time = job.time
                        print(str(time))
                        now = datetime.datetime.utcnow().replace(tzinfo=timezone.utc)
                        print(str(now))
                        while time < now:
                            if job.typeofbackup == 1:
                                increase_day = 1
                            elif job.typeofbackup == 2:
                                increase_day = 7
                            time = job.time + datetime.timedelta(days=increase_day)

                        schedule = Schedule(time=time, typeofbackup=job.typeofbackup,
                                            ip_server=job.ip_server, computer=computer, path=job.path)
                        schedule.save()
            elif request_data['status_code'] == 404:
                # remove job
                job = Schedule.objects.get(id=request_data['job_id'])
                job.delete()

                # logging
            return HttpResponse("OK")
        else:
            return HttpResponse('Unauthorized', status=401)


@csrf_exempt
def update_info_agent(request):
    if request.method == 'POST':
        computer = get_computer_by_token(request)
        if computer:
            request_data = json.loads(request.body.decode())
            print(request_data)
            computer.ram = request_data['mem_total']
            computer.cpu = request_data['cpus']
            computer.platform = request_data['platform']
            computer.save()

            return HttpResponse("OK")
        else:
            return HttpResponse('Unauthorized', status=401) 