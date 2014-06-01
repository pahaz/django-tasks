from django.conf.urls import patterns, url
from audios import views

urlpatterns = patterns('', 
   # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
	url(r'^upload', views.upload_file, name='upload'),
	url(r'^test', views.test, name='test'),
    url(r'^login', views.site_login, name='login'),
    url(r'^logout', views.site_logout, name='logout'),
	# url(r'^download/(?P<audio_id>\d+)/$', views.download, name='download'),

    # url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)