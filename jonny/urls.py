from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^admin/lookfor$', 'matching.views.prescrap'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/venues/reca', 'matching.views.reca'),
    url(r'^api/venues/activities', 'matching.views.activities'),
    url(r'^api/venues/accommodations', 'matching.views.accommodations'),
    url(r'^api/venues/beaches', 'matching.views.beaches'),

    url(r'^api/charge', 'plan.views.charge'),
    url(r'^api/upload', 'upload.views.upload'),

    url(r'^api/notifications/user_registered', 'notifications.views.registered'),
    url(r'^api/notifications/user_charged', 'notifications.views.got_plan'),
    url(r'^api/notifications/plan_ready', 'notifications.views.plan_ready'),
    url(r'^api/notifications/wolf_chat', 'notifications.views.wolf_chat'),
    url(r'^api/notifications/jonny_chat', 'notifications.views.jonny_chat'),
    url(r'^api/notifications/user_chat', 'notifications.views.user_chat'),
)
