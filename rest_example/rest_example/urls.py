from django.conf.urls import patterns, include, url
from django.contrib import admin
from restapp import views

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),)
