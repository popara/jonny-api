from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('matching.views',
    url(r'^job/start/(?P<job_id>(.+))', 'start_job'),
    url(r'^job/apply/(?P<job_id>(.+))/(?P<user_id>(.+))', 'job_apply'),
)
