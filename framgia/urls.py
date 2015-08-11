from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index.index, name='index'),
                       url(r'^blog/', views.blog.index, name='blog'),
                       url(r'^(?P<blog_id>[0-9]+)/$', views.blog.detail, name='blog_detail'),
                       url(r'^contact/', views.contact.index, name='contact'),
                       url(r'^contact_post/$', views.contact.contact_post, name='contact_post'),
                       )
