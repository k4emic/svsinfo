from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

import serializers
import models

@api_view(['GET'])
def api_home(request):
    return Response({
        'conventions': reverse('convention-list', request=request),
    })
    
class ConventionsList(generics.ListAPIView):
    model = models.Convention
    serializer_class = serializers.ConventionListSerializer
    
class ConventionDetail(generics.RetrieveAPIView):
    model = models.Convention
    serializer_class = serializers.ConventionSerializer
    
class LocationsList(generics.ListAPIView):
    model = models.Location
    serializer_class = serializers.LocationSerializer
    
class LocationDetail(generics.RetrieveAPIView):
    model = models.Location
    serializer_class = serializers.LocationSerializer
    
class EventList(generics.ListAPIView):
    model = models.Event
    serializer_class = serializers.EventSerializer
    
class EventDetail(generics.RetrieveAPIView):
    model = models.Event
    serializer_class = serializers.EventSerializer

class AreaList(generics.ListAPIView):
    model = models.Area
    serializer_class = serializers.AreaSerializer

class AreaDetail(generics.RetrieveAPIView):
    model = models.Area
    serializer_class = serializers.AreaSerializer

class NewsList(generics.ListAPIView):
    model = models.NewsItem
    serializer_class = serializers.NewsItemSerializer

class NewsDetail(generics.RetrieveAPIView):
    model = models.NewsItem
    serializer_class = serializers.NewsItemSerializer
