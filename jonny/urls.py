from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/lookfor$', 'matching.views.prescrap'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/venues/reca', 'matching.views.reca'),
    url(r'^api/venues/activities', 'matching.views.activities'),
    url(r'^api/venues/accommodations', 'matching.views.accommodations'),
    url(r'^api/venues/beaches', 'matching.views.beaches'),


    url(r'^api/csrf', 'plan.views.csrf'),
    url(r'^api/charge', 'plan.views.charge'),
    url(r'^api/upload', 'plan.views.upload'),
)
