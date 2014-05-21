from django.conf.urls import url
from music import views


urlpatterns = [
    url(r'^$', views.all_tracks),
    url(r'^history/$', views.history, name='history'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.log_in, name='login'),
    url(r'^logout$', views.log_out, name='logout'),
    url(r'^pushToHistory$', views.push_to_history, name='push_to_history')
]
