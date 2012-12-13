from django.conf.urls import patterns, url
from rest_framework.generics import ListAPIView, RetrieveAPIView
from views import ConventionsList, LocationsList, ConventionDetail, LocationDetail
from serializers import AreaSerializer
from models import Area

urlpatterns = patterns('service.views',
    url(r'^$', 'api_home'),
    
    url(r'^conventions/$', ConventionsList.as_view(), name='convention-list'),
    url(r'^conventions/(?P<slug>\d{4})/$', ConventionDetail.as_view(), name='convention-detail'),
    
    url(r'^locations/$', LocationsList.as_view(), name='location-list'),
    url(r'^locations/(?P<pk>\d+)/$', LocationDetail.as_view(), name='location-detail'),
    
    url(r'^areas/$', ListAPIView.as_view(model=Area, serializer_class=AreaSerializer), name='area-list'),
    url(r'^areas/(?P<pk>\d+)/$', RetrieveAPIView.as_view(model=Area, serializer_class=AreaSerializer), name='area-detail'),

)
