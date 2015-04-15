from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/lookfor$', 'matching.views.prescrap'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/account/', include('authentication.urls')),
)
