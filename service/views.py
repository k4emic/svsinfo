from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from serializers import ConventionSerializer, ConventionListSerializer, LocationSerializer
from models import Convention, Location

@api_view(['GET'])
def api_home(request):
    return Response({
        'conventions': reverse('convention-list', request=request),
    })
    
    
class ConventionDetail(generics.RetrieveAPIView):
    model = Convention
    serializer_class = ConventionSerializer
    
class ConventionsList(generics.ListAPIView):
    model = Convention
    serializer_class = ConventionListSerializer

class LocationsList(generics.ListAPIView):
    model = Location
    serializer_class = LocationSerializer
    
    
class LocationDetail(generics.RetrieveAPIView):
    model = Location
    serializer_class = LocationSerializer

