from django.conf.urls import url
from . import views

urlpatterns = [ 
	url(r'^home/$', views.home, name='page_home'),
	url(r'^about/$', views.about, name='page_about'),
	url(r'^contact/$', views.contact, name='page_contact'),
	url(r'^excel/$', views.export_users_xls, name='page_export_xls'),
	url(r'^pdf/$', views.export_pdf, name='export_pdf'),
]