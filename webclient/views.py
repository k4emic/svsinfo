from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    context = {'message': 'Hello world!'}
    return render_to_response('hello.html', context, RequestContext(request))
    