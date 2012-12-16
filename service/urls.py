from django.conf.urls import patterns, url
import views

urlpatterns = patterns('service.views',
    url(r'^$', 'api_home'),
    
    url(r'^conventions/$', views.ConventionsList.as_view(), name='convention-list'),
    url(r'^conventions/(?P<pk>\d+)/$', views.ConventionDetail.as_view(), name='convention-detail'),
    
    url(r'^locations/$', views.LocationsList.as_view(), name='location-list'),
    url(r'^locations/(?P<pk>\d+)/$', views.LocationDetail.as_view(), name='location-detail'),
    
    url(r'^areas/$', views.AreaList.as_view(), name='area-list'),
    url(r'^areas/(?P<pk>\d+)/$', views.AreaDetail.as_view(), name='area-detail'),
    
    url(r'^events/$', views.EventList.as_view(), name='event-list'),
    url(r'^events/(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event-detail'),
    
    url(r'^news/$', views.NewsList.as_view(), name='news-list'),
    url(r'^news/(?P<pk>\d+)/$', views.NewsDetail.as_view(), name='news-detail'),
)
