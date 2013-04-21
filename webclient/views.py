from django.shortcuts import render_to_response
from django.template import RequestContext
from service import models
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
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
        
    events = con.events_on_day(active_weekday).prefetch_related('newsitem_set', 'area')
    news_items = con.newsitem_set.all()
    
    
    context = {
        'weekdays': weekdays,
        'active_weekday': active_weekday,
        'convention': con,
        'events': events,
        'news_items': news_items
    }
    
    return render_to_response('index.html', context, RequestContext(request))
