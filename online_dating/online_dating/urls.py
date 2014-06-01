from django.conf.urls import patterns, include, url

from django.contrib import admin

from profiles import views as profile_views
from auth_app import views as auth_views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


from django.conf import settings
from django.conf.urls.static import static





urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'online_dating.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', profile_views.random_profiles, name='index'),
    url(r'^profiles/', include('profiles.urls'), name='profiles'),

	# authentication
	url(r'^accounts/login/$', auth_views.auth_view, name='login'),
	url(r'^accounts/logout/$', auth_views.logout, name='logout'),
	url(r'^accounts/register/$', auth_views.register_user, name='register'),
    url(r'^accounts/invalid/$', auth_views.auth_only, name='auth_only'),

	# filters
    url(r'^(?P<filter>other|m|f)$', profile_views.display_objects_with_filter),
    url(r'^most_commented$', profile_views.most_commented),
	url(r'^most_rated$', profile_views.most_rated),
)



if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()