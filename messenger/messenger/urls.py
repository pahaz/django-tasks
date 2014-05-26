from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='/login/')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'chat.views.login'),
    url(r'^registration/$', 'chat.views.registration'),
    url(r'^logout/$', 'chat.views.logout'),
    url(r'^add/(.*)$', 'chat.views.add_to_friends'),
    url(r'^reject/(.*)$', 'chat.views.reject'),
    url(r'^remove/(.*)$', 'chat.views.remove_from_friends'),
    url(r'^account/$', 'chat.views.account'),
    url(r'^contacts/$', 'chat.views.contacts'),
    url(r'^chat/with/(.*)$', 'chat.views.chat_with'),
    url(r'^unread/with/(.*)$', 'chat.views.unread_with'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
)
