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
    url(r'^contact/$', views.UsersView.as_view(), name='contact'),
    url(r'^networking/$', views.interface, name='networking'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page' : 'login'}, name='logout'),
    url(r'^reboot/$', views.reboot, name='reboot'),
<<<<<<< HEAD
    url(r'^agent/$', views.agent, name='agent'),
    url(r'^manage-agent/$', views.manage_agent, name='manage-agent'),
=======
    url(r'^agent/$', views.Agent.as_view(), name='agent'),
>>>>>>> 2ab29557f033756a9cc78fd83b209ddc3c161e8a
]
