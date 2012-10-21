from django.conf.urls import patterns, url
from service.model_resources import LocationResource, AreaResource, EventResource, ActivityResource, NewsItemResource

# rest framework
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

urlpatterns = patterns('',
    # /events 
    url(r'^events/$', ListOrCreateModelView.as_view(resource=EventResource)),
    # /events/<id>
    url(r'^events/(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=EventResource), name="event"),
    
    # /events/<event>/activities
    url(r'^events/(?P<event>[\d]+)/activities/$', ListOrCreateModelView.as_view(resource=ActivityResource), name="activities"),
    # /activities/<id>
    url(r'^activities/(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=ActivityResource), name="activity"),
    
    # locations/<id>
    url(r'^locations/(?P<pk>[\d]+)/$', ListOrCreateModelView.as_view(resource=LocationResource), name="location"),
    # locations/<id>/areas
    url(r'^locations/(?P<location>[\d]+)/areas/$', ListOrCreateModelView.as_view(resource=AreaResource), name="areas"),
    # areas/<id>
    url(r'^areas/(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=AreaResource), name="area"),
    
    # /activity/<id>/news
    url(r'^activity/(?P<activity>[\d]+)/news/$', ListOrCreateModelView.as_view(resource=NewsItemResource), name='activity-news'),
    # /events/<event-id>/news
    url(r'^events/(?P<event>[\d]+)/news/$', ListOrCreateModelView.as_view(resource=NewsItemResource), name="event-news"),
    
)
