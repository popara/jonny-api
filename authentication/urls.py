from django.conf.urls import patterns, include, url

from views import register

urlpatterns = patterns('',
    url(r'register$', register, name="register"),
)
