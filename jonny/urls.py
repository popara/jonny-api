from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jonny.views.home', name='home'),
    url(r'^admin/lookfor$', 'matching.views.prescrap'),

    url(r'^admin/', include(admin.site.urls)),
)
