from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movie/$', 'movie.views.movie_list'),
    url(r'^movie/(\d+)/$', 'movie.views.movie'),
    url(r'^movie/(\d+)/add/$', 'movie.views.buy'),
    url(r'^movie/thanks/$', 'movie.views.thanks'),
    url(r'^$', 'core.views.index_page'),
    url(r'^login/$', 'movie.views.login'),
    url(r'^registration/$', 'movie.views.registration'),
    url(r'^logout/$', 'movie.views.logout'),
    url(r'^account/$', 'movie.views.account'),
    url(r'^account/edit/$', 'movie.views.account_edit'),
    url(r'^pay/$', 'movie.views.paypage'),
    url(r'^paying/$', 'movie.views.pay')
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)