from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^$', views.index, name='index'),
	url(r'^time/$', views.get_time, name='time'),
	url(r'^template/$', views.template_view, name='template'),
	url(r'^userlist/$', views.userlist, name='userlist'),
]