from django.conf.urls import patterns, url
from service.model_resources import LocationResource, AreaResource, EventResource, ActivityResource, NewsItemResource

# rest framework
from djangorestframework.views import InstanceModelView
from service.views import AuthListOrCreateView

urlpatterns = patterns('',
    # /events 
    url(r'^events/$', AuthListOrCreateView.as_view(resource=EventResource)),
    # /events/<id>
    url(r'^events/(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=EventResource), name="event"),
    
    # /events/<event>/activities
    url(r'^events/(?P<event>[\d]+)/activities/$', AuthListOrCreateView.as_view(resource=ActivityResource), name="activities"),
    # /activities/<id>
    url(r'^activities/(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=ActivityResource), name="activity"),
    
    # locations/<id>
    url(r'^locations/(?P<pk>[\d]+)/$', AuthListOrCreateView.as_view(resource=LocationResource), name="location"),
    # locations/<id>/areas
    url(r'^locations/(?P<location>[\d]+)/areas/$', AuthListOrCreateView.as_view(resource=AreaResource), name="areas"),
    # areas/<id>
    url(r'^areas/(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=AreaResource), name="area"),
    
    # /activity/<id>/news
    url(r'^activity/(?P<activity>[\d]+)/news/$', AuthListOrCreateView.as_view(resource=NewsItemResource), name='activity-news'),
    # /events/<event-id>/news
    url(r'^events/(?P<event>[\d]+)/news/$', AuthListOrCreateView.as_view(resource=NewsItemResource), name="event-news"),
    
)
