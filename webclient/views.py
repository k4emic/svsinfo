from django.shortcuts import render_to_response
from django.template import RequestContext
from service import models
import django.utils.timezone
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    
    now = django.utils.timezone.now()
    
    current_events = []
    future_events = []
    past_events = []
    weekdays = {}
    
    # get current con
    con = models.Convention.current()
    dates = con.dates()
    
    for date in dates: # build list of weekdays
        weekdays[date.isoweekday()] = date.strftime('%A')
        
    active_weekday = dates[0].isoweekday() 
    if('day' in request.GET):
        try:
            active_weekday = int(request.GET['day'])
        except ValueError:
            pass
        
    events = con.events_on_day(active_weekday).select_related('news_item', 'area')
    news_items = con.newsitem_set.all()
    
    

    for event in events:
        if(event.start_time < now and now < event.end_time): # current event
            current_events.append(event)
        elif(event.end_time > now): # future event
            future_events.append(event)
        else:
            past_events.append(event) # past event
            
    context = {
        'weekdays': weekdays,
        'active_weekday': active_weekday,
        'convention': con,
        'current_events': current_events,
        'future_events': future_events,
        'past_events': past_events,
        'news_items': news_items
    }
    
    return render_to_response('index.html', context, RequestContext(request))
