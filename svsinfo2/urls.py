from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('webclient.urls')),
    url(r'^api/', include('service.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
