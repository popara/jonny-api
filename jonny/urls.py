from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^admin/lookfor$', 'matching.views.prescrap'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/charge', 'plan.views.charge'),
    url(r'^api/upload', 'upload.views.upload'),

    url(r'^api/notifications/user_registered', 'notifications.views.registered'),
    url(r'^api/notifications/user_charged', 'notifications.views.got_plan'),
    url(r'^api/notifications/plan_ready', 'notifications.views.plan_ready'),
    url(r'^api/notifications/wolf_chat', 'notifications.views.wolf_chat'),
    url(r'^api/notifications/jonny_chat', 'notifications.views.jonny_chat'),
    url(r'^api/notifications/user_chat', 'notifications.views.user_chat'),
    url(r'^api/', include('matching.urls')),
    url(r'^api/', include('round_robin.urls')),
)
