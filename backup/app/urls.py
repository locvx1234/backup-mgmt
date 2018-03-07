from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^networking/$', views.interface, name='networking'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page' : 'login'}, name='logout'),
    url(r'^reboot/$', views.reboot, name='reboot'),
]
