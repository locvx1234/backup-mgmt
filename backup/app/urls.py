from django.conf.urls import url
from app import views
from django.contrib.auth import views as auth_views
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^networking/$', views.networking, name='networking'),
    url(r'^device_setting/$', views.device_setting, name='device_setting'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page' : 'login'}, name='logout'),
    url(r'^reboot/$', views.reboot, name='reboot'),
    url(r'^config-agent/(?P<computer_id>\d+)/$', views.config_agent, name='config-agent'),
    url(r'^agent/$', views.agent, name='agent'),
    url(r'^restore/$', views.restore, name='restore'),
    url(r'^off-site/$', views.off_site_sync, name='off_site'),
    url(r'^delete-agent/(?P<agent_id>\d+)/$', views.delete_agent, name='agent_delete'),
    url(r'^recover-point/(?P<agent_id>\d+)/$', views.recover_point, name='agent-recover-point'),
    url(r'^delete-sync/(?P<sync_id>\d+)/$', views.delete_sync, name='sync_delete'),
    url(r'^delete-schedule/(?P<schedule_id>\d+)/$', views.delete_schedule, name='schedule_delete'),
]
