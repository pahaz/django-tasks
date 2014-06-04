from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns('',
    url(r'^(?P<profile_id>[0-9]+)/$', views.detail),
    url(r'^create/$', views.create_profile, name='create'),
)