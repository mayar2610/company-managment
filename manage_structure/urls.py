from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.company_list, name='company_list'),
	url(r'^company/(?P<pk>[0-9]+)/$', views.company_detail, name='company_detail'),
	url(r'^company/new/$', views.company_new, name='company_new'),
	url(r'^company/(?P<pk>[0-9]+)/edit/$', views.company_edit, name='company_edit'),
	url(r'^company/(?P<pk>\d+)/remove/$', views.company_remove, name='company_remove'),
]