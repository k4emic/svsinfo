from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.response import Response

from serializers import ConventionSerializer
from models import Convention

@api_view(['GET'])
def api_home(request, format=None):
    return Response({
        'conventions': reverse('convention-list', request=request),
    })
    
    
class ConventionsList(generics.ListAPIView):
    model = Convention
    serializer_class = ConventionSerializer
    
    def get_queryset(self):
        
        queryset = Convention.objects.all()
        queryset.filter()
        
        if('year' in self.kwargs):
            year = self.kwargs['year']
            queryset = queryset.filter(start_time__year=year)
        
        return queryset
        

