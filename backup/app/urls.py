from django.conf.urls import url
from app import views
from django.contrib.auth import views as auth_views
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)


urlpatterns = [
    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^networking/$', views.networking, name='networking'),
    url(r'^device_setting/$', views.device_setting, name='device_setting'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page' : 'login'}, name='logout'),
    url(r'^reboot/$', views.reboot, name='reboot'),
    url(r'^config-agent/(?P<agent_id>\d+)/$', views.config_agent, name='config-agent'),
    url(r'^restore-agent/(?P<agent_id>\d+)/$', views.restore_agent, name='restore-agent'),
    url(r'^restore-agent/(?P<agent_id>\d+)/cancel/(?P<restore_id>\d+)/$', views.restore_cancel, name='restore-cancel'),
    url(r'^agent/$', views.agent, name='agent'),
    url(r'^agent/(?P<agent_id>\d+)/$', views.agent, name='start_backup'),
    url(r'^off-site/$', views.off_site_sync, name='off_site'),
    url(r'^delete-agent/(?P<agent_id>\d+)/$', views.delete_agent, name='agent_delete'),
    url(r'^recover-point/(?P<agent_id>\d+)/$', views.recover_point, name='agent-recover-point'),
    url(r'^delete-sync/(?P<sync_id>\d+)/$', views.delete_sync, name='sync_delete'),
    url(r'^delete-schedule/(?P<schedule_id>\d+)/$', views.delete_schedule, name='schedule_delete'),
    url(r'^api/get-job/$', views.get_job, name='get-job'),
    url(r'^api/result-backup/$', views.handle_result_backup, name='handle-result-backup'),
    url(r'^api/result-restore/$', views.handle_result_restore, name='handle-result-restore'),
    url(r'^api/info-agent/$', views.update_info_agent, name='update-info-agent'),
]
