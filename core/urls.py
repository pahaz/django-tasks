from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movie/', 'movie.views.movie_list'),
    url(r'^$', 'core.views.index_page'),
    url(r'^login/$', 'movie.views.login'),
    url(r'^registration/$', 'movie.views.registration'),
    url(r'^logout/$', 'movie.views.logout'),
    url(r'^account/$', 'movie.views.account'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)