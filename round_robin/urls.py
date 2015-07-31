from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('round_robin.views',
    url(r'round_robin$', 'round_robin'),
)
