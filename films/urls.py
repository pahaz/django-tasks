from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf.urls.static import static
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'films.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'movie.views.main'),
    url(r'^movie', 'movie.views.index'),
    url(r'^contacts', 'movie.views.contacts'),
)