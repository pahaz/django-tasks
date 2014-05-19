from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project_Django_Course.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^my_books/$', 'Book.views.my_books'),
    url(r'^my_books/choice/$', 'Book.views.choice'),
    url(r'^my_books/choice/accepted/$', 'Book.views.accepted'),
    url(r'^page/(\d+)/$', 'Book.views.books'),
    url(r'^books/add_like/(\d+)/$', 'Book.views.add_like'),
    url(r'^books/get/(\d+)/$', 'Book.views.only_one_book'),
    url(r'^books/get/(\d+)/add_in_list/$', 'Book.views.add_in_list'),
    url(r'^books/get/(\d+)/buy/thx/$', 'Book.views.thx'),
    url(r'^books/add_comment/(\d+)/$', 'Book.views.add_comment'),
    url(r'^$', 'Book.views.books'),
)


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
