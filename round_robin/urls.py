from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('round_robin.views',
    url(r'round_robin/(?P<robin_id>[0-9])$', 'round_robin'),
)
