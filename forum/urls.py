from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name = 'index'),
                       url(r'^(?P<page_num>\d+)$', views.IndexView.as_view(), name='index_page'),
                       url(r'^theme/(?P<pk>\d+)$', views.DetailsView.as_view(), name = 'theme_mess'),
                       url(r'^theme/(?P<pk>\d+)/add_message$', views.add_message, name = 'add_message'),
                       url(r'^login$', views.LoginView.as_view(), name = 'login_page'),
                       url(r'^logout$', views.logout_view, name = 'logout'),
                       url(r'^register$', views.RegisterView.as_view(), name = 'register'),
                       url(r'^add_theme$', views.add_theme, name = 'add_theme'),
                       url(r'^theme/(?P<tpk>\d+)/delete_mess/(?P<mpk>\d+)', views.delete_message, name = 'delete_mess'),
                       url(r'^theme/(?P<tpk>\d+)/edit_mess/(?P<mpk>\d+)', views.edit_mess_page, name = 'edit_mess'),
                       )
