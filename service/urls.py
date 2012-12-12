from django.conf.urls import patterns, url
from views import ConventionsList

urlpatterns = patterns('service.views',
    url(r'^$', 'api_home'),
    url(r'^conventions/$', ConventionsList.as_view(), name='convention-list'),
    url(r'^conventions/(?P<year>\d{4})/$', ConventionsList.as_view(), name='convention-detail'),

)
