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

def reboot(request):
    os.system('reboot')
    return
