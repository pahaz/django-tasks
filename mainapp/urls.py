# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('mainapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^list/$', 'list', name='list'),
    url(r'^register/$', 'register', name='register'),
    url(r'^login/$', 'user_login', name='login'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^logout/$', 'user_logout', name='logout'),
    url(r'^get_credits/$', 'get_credits', name='get_credits'),
    url(r'^download/(?P<document_id>\d+)$', 'download', name='download'),
)
