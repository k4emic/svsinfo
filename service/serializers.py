from service.models import Convention, Event, Location, Area, NewsItem
from rest_framework import serializers;

class ConventionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Convention
        fields = ('name', 'start_time', 'end_time', 'location')
