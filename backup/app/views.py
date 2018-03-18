import sys
import os
import fileinput

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

import yaml
import netifaces
import pytz
##########################
from .models import Computer
from django.views import generic 
from netaddr import *

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

def index(request):
    if request.user.is_authenticated:
        pass
    else:
        return HttpResponseRedirect('/login')

    context = {}
    ### find a public IP, if cant get a private instead
    interfaces = [x for x in get_all_interface() if x['ip'] != 'Disable']
    private_ip = None
    public_ip = None
    for interface in interfaces:
        if not IPAddress(interface['ip']).is_private() and not IPAddress(interface['ip']).is_loopback():
            public_ip = interface['ip']
        elif not private_ip:
            private_ip = interface['ip']
    if not public_ip:
        context['ip'] = private_ip
        context['ip_type'] = 'private'
    else:
        context['ip'] = public_ip
        context['ip_type'] = 'public'
    ### get all computer and disk used with each computer
    all_computer = Computer.objects.all()
    context['agents'] = all_computer
    disk_used_obs = []

    for computer in all_computer:
        disk_used = {}
        volumes = computer.volume_set.all()
        for volume in volumes:
            print(volume.__str__())
            last_sync = volume.sync_set.all()[0]
            print(last_sync.capacity_used)
            used_disk = last_sync.capacity_used
        disk_used_obs.append({'name': computer.name, 'used_disk': used_disk})
    context['agents_count'] = len(context['agents'])
    context['disk_used'] = disk_used_obs
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
    timezone = settings.TIME_ZONE
    list_timezone = pytz.all_timezones
    if request.method == 'POST':
        timezone = request.POST.get('timezone-select')
        # change TIME_ZONE in settings.py
        for line in fileinput.input(settings.BASE_DIR + '/backup/settings.py', inplace=True):
            if line.strip().startswith('TIME_ZONE = '):
                line = 'TIME_ZONE = ' + "'" + timezone + "'\n"
            sys.stdout.write(line)
    return render(request, 'app/device_setting.html', {'timezone': timezone, 'list_tz': list_timezone})


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
                line = line.split( '#', 1 )[ 0 ]
                line = line.rstrip()
                if 'nameserver' in line:
                    resolvers.append( line.split()[ 1 ] )
                if 'search' in line:
                    dns['search'] = line.split()[ 1 ]
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
    agents = Computer.objects.all()
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
        agent = Computer(serial_number = serial, name = name, ip_address = ip, ram = ram, os = os, cpu = cpu,
                         agent_version = version )
        agent.save()
    return render(request, 'app/agent.html', {'agents': agents})    

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
    return render(request, 'app/contact.html', {'data_contact': data_loaded, 'user_list':user_list} )

# def error_404(request):
#         return render(request,'app/page_404.html', status=404)
#
# def error_500(request):
#         return render(request,'app/page_500.html', status=500)
