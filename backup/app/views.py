from django.shortcuts import render
from django.template import loader
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
import os
from django.contrib.auth.models import User
from django.views.generic import TemplateView

import netifaces
##########################
from .models import Computer
from django.views import generic 

def index(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'app/index.html', context)
    else:
        return HttpResponseRedirect('/login')


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


def interface(request):
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
    return render(request, 'app/networking.html', {'interfaces': interfaces})


def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr

class UsersView(TemplateView):
    template_name = 'app/contact.html'

    def get_context_data(self, **kwargs):
        context = super(UsersView,self).get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context


def agent(request):
    agents = get_object_or_404(Computer)
    return render(request, 'app/agent.html', {'agents': agents})    
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        name = request.POST.get('agent-name','')
        os = request.POST.get('agent-os','')
        ip = request.POST.get('agent-ip','')
        serial = request.POST.get('agent-serial','')
        ram = request.POST.get('agent-ram','')
        agent = Agent(serial_number = serial, name = name, ip_address = ip, ram = ram, os = os)
        agent.save()

def magage_agent(request):
    context = {}
    return render(request, 'app/manage_recover_point.html', context)

class Agent(generic.ListView):
    template_name = 'app/agent.html'
    context_object_name = 'agents'
    def get_queryset(self):
        return Computer.objects.all()


