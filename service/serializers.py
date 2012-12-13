from service.models import Convention, Location, Area, Event
from rest_framework import serializers

class ConventionListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Convention
        fields = ('url', 'name', 'start_time', 'end_time')

class ConventionSerializer(serializers.HyperlinkedModelSerializer):
    
    events = serializers.ManyHyperlinkedRelatedField(source='event_set', view_name='event-detail')
    
    class Meta:
        model = Convention
        fields = ('name', 'start_time', 'end_time', 'location', 'events')
        

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    
    areas = serializers.ManyHyperlinkedRelatedField(source='area_set', view_name='area-detail')
    
    class Meta:
        model = Location
        fields = ('name', 'areas')
        
        
class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('name', 'location')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'url', 'convention', 'area')

