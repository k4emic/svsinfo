from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from serializers import ConventionSerializer, LocationSerializer
from models import Convention, Location

@api_view(['GET'])
def api_home(request):
    return Response({
        'conventions': reverse('convention-list', request=request),
    })
    
    
class ConventionDetail(generics.RetrieveAPIView):
    model = Convention
    serializer_class = ConventionSerializer
    slug_field = 'start_time__year'
    
    def get_queryset(self):
        
        queryset = Convention.objects.all()
        queryset.filter()
        
        if('year' in self.kwargs):
            year = self.kwargs['year']
            queryset = queryset.filter(start_time__year=year)
        
        return queryset
    
    
class ConventionsList(generics.ListAPIView):
    model = Convention
    serializer_class = ConventionSerializer


class LocationsList(generics.ListAPIView):
    model = Location
    serializer_class = LocationSerializer
    
    
class LocationDetail(generics.RetrieveAPIView):
    model = Location
    serializer_class = LocationSerializer

