from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    return render(request, 'app/' + load_template, context)
