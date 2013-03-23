from django.shortcuts import render_to_response
from django.template import RequestContext
from service import models
import django.utils.timezone

# Create your views here.
def index(request):
    # get current con
    con = models.Convention.current()
    events = con.event_set.order_by('start_time').select_related('news_item', 'area').all()
    news_items = con.newsitem_set.all()
    
    current_events = []
    future_events = []
    past_events = []
    
    now = django.utils.timezone.now()
    for event in events:
        if(event.start_time < now and now < event.end_time): # current event
            current_events.append(event)
        elif(event.end_time > now): # future event
            future_events.append(event)
        else:
            # past events are not interesting
            past_events.append(event)
    
    context = {
        'convention': con,
        'current_events': current_events,
        'future_events': future_events,
        'past_events': past_events,
        'news_items': news_items
        
    }
    
    return render_to_response('index.html', context, RequestContext(request))
