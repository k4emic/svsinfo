from service.models import Convention, Location, Area, Event, NewsItem
from rest_framework import serializers

class ConventionListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Convention
        fields = ('name', 'start_time', 'end_time')

class ConventionSerializer(serializers.ModelSerializer):
    
    events = serializers.ManyHyperlinkedRelatedField(source='event_set', view_name='event-detail')
    
    class Meta:
        model = Convention
        fields = ('name', 'start_time', 'end_time', 'location', 'events')
        

class LocationSerializer(serializers.ModelSerializer):
    
    areas = serializers.ManyHyperlinkedRelatedField(source='area_set', view_name='area-detail')
    
    class Meta:
        model = Location
        fields = ('name', 'areas')
        
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('name', 'location')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'convention', 'area')


class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ('title', 'time', 'convention', 'event')


