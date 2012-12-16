from django.conf.urls import patterns, url
from rest_framework.generics import ListAPIView, RetrieveAPIView
from views import ConventionsList, LocationsList, ConventionDetail, LocationDetail
from serializers import AreaSerializer, EventSerializer, NewsItemSerializer
from models import Area, Event, NewsItem

urlpatterns = patterns('service.views',
    url(r'^$', 'api_home'),
    
    url(r'^conventions/$', ConventionsList.as_view(), name='convention-list'),
    url(r'^conventions/(?P<pk>\d+)/$', ConventionDetail.as_view(), name='convention-detail'),
    
    url(r'^conventions/(?P<pk>\d+)/events/$', ListAPIView.as_view(model=Event, serializer_class=EventSerializer)),
    
    url(r'^locations/$', LocationsList.as_view(), name='location-list'),
    url(r'^locations/(?P<pk>\d+)/$', LocationDetail.as_view(), name='location-detail'),
    
    url(r'^areas/$', ListAPIView.as_view(model=Area, serializer_class=AreaSerializer), name='area-list'),
    url(r'^areas/(?P<pk>\d+)/$', RetrieveAPIView.as_view(model=Area, serializer_class=AreaSerializer), name='area-detail'),
    
    url(r'^events/$', ListAPIView.as_view(model=Event, serializer_class=EventSerializer), name='event-list'),
    url(r'^events/(?P<pk>\d+)/$', RetrieveAPIView.as_view(model=Event, serializer_class=EventSerializer), name='event-detail'),
    
    url(r'^news/$', ListAPIView.as_view(model=NewsItem, serializer_class=NewsItemSerializer), name='news-list'),
    url(r'^news/(?P<pk>\d+)/$', RetrieveAPIView.as_view(model=NewsItem, serializer_class=NewsItemSerializer), name='news-detail'),
)
