import sys
import os
import fileinput
import datetime

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

import yaml
import netifaces
import pytz
from bs4 import BeautifulSoup

##########################
from .models import Computer, Sync
from django.views import generic
from ipaddress import ip_address
from django.shortcuts import redirect
from django.urls import reverse_lazy


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
        used_disk = 0
        syncs_of_computer = computer.sync_set.all()
        last_sync = syncs_of_computer[0]
        print(last_sync.sync_time)
        used_disk = 0
        for sync in syncs_of_computer:
            used_disk += sync.amount_data_change
        disk_used_obs.append({'name': computer.name, 'used_disk': used_disk})
        last_sync_obs.append({'name': computer.name, 'last_sync_time': last_sync.sync_time})
    ###
    context['agents_count'] = len(context['agents'])
    context['disk_used'] = disk_used_obs
    context['last_syncs'] = last_sync_obs
    for disk_used_ob in disk_used_obs:
        total_protect_data += disk_used_ob['used_disk']

    context['total_protect_data'] = total_protect_data

    context['ip_offsite'] = settings.OFFSITE_SERVER
    context['speed_limit'] = settings.OFFSITE_LIMIT_SPEED
    return render(request, 'app/index.html', context)
    

def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    return render(request, 'app/' + load_template, context)


def reboot():
    os.system('reboot')
    return


def device_setting(request):
    # get timezone
    timezone = settings.TIME_ZONE
    list_timezone = pytz.all_timezones

    # get time to refresh page
    with open("app/templates/app/base_site.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    meta_refresh = soup.findAll(attrs={"http-equiv": "refresh"})
    time_refresh = str(meta_refresh[0]['content'])

    if request.method == 'POST':

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

    return render(request, 'app/device_setting.html', {'timezone': timezone, 'list_tz': list_timezone, 'time_refresh': time_refresh})


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


def agent(request):
    agents_info = []
    agents = Computer.objects.all()
    data_used = 0
    for agent in agents:
        agent_syncs = agent.sync_set.all()
        if agent_syncs :
            last_sync = agent_syncs[0]
        else:
            last_sync = None
        for sync in agent_syncs:
            data_used+=sync.amount_data_change
        agents_info.append({'agent':agent, 'data_used': data_used, 'last_sync_time': last_sync.sync_time if last_sync else None })
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        name = request.POST.get('agent-name','')
        os = request.POST.get('agent-os','')
        ip = request.POST.get('agent-ip','')
        serial = request.POST.get('agent-serial','')
        ram = request.POST.get('agent-ram','')
        cpu = request.POST.get('agent-cpu','')
        version = request.POST.get('agent-version','')
        capacity_used = request.POST.get('agent-capacity-used')
        agent = Computer(serial_number = serial, name = name, ip_address = ip, ram = ram, os = os, cpu = cpu, capacity_used = capacity_used, agent_version = version )
        agent.save()
    return render(request, 'app/agent.html', {'agents': agents_info})


def delete_agent(request, agent_id):
    agent = Computer.objects.filter(id = agent_id)
    agent.delete()
    return HttpResponseRedirect('/agent')

def restore(request):
    agents = Computer.objects.all()
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        name = request.POST.get('agent-name','')
        os = request.POST.get('agent-os','')
        ip = request.POST.get('agent-ip','')
        serial = request.POST.get('agent-serial','')
        ram = request.POST.get('agent-ram','')
        agent = Computer(serial_number = serial, name = name, ip_address = ip, ram = ram, os = os)
        agent.save()
    return render(request, 'app/restore.html', {'agents': agents})


def config_agent(request):
    context = {}
    return render(request, 'app/config_agent.html', context)


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
                  {'data_change': data_change, 'ip_offsite': ip_offsite, 'speed_limit': speed_limit})