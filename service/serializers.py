from service.models import Convention, Location, Area
from rest_framework import serializers

class ConventionSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Convention
        fields = ('name', 'start_time', 'end_time', 'location')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    
    areas = serializers.ManyHyperlinkedRelatedField(source='area_set', view_name='area-detail')
    
    class Meta:
        model = Location
        fields = ('name', 'areas')
        
        
class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('name', 'location')
