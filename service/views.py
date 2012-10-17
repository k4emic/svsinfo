from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    t = loader.get_template("service/index")
    c = Context({
        'foo': 'bar'
    })
    
    return HttpResponse(t.render(c))