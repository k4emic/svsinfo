from django.conf.urls import patterns, url
from service.model_resources import LocationResource, AreaResource, EventResource, ActivityResource, NewsItemResource

# rest framework
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

urlpatterns = patterns('',
    # /events 
    url(r'^events/$', ListOrCreateModelView.as_view(resource=EventResource)),
    # /events/<id>
    url(r'^events/(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=EventResource)),
    
    # /events/<event>/activities
    url(r'^events/(?P<event>[\d]+)/activities/$', ListOrCreateModelView.as_view(resource=ActivityResource)),
    # /events/<event>/activities/<id>
    url(r'^events/(?P<event>[\d]+)/activities/(?P<pk>[\d]+)/$', InstanceModelView.as_view(resource=ActivityResource)),
    
    # /locations
    url(r'^locations/$', ListOrCreateModelView.as_view(resource=LocationResource)),
    # /locations/<id>/areas
    url(r'^locations/(?P<location>[\d]+)/areas/$', ListOrCreateModelView.as_view(resource=AreaResource)),
    
    # /events/<event-id>/news
    url(r'^events/(?P<event>[\d]+)/news/$', ListOrCreateModelView.as_view(resource=NewsItemResource)),
    
    # /events/<event-id>/news/<id>
    url(r'^events/(?P<event>[\d]+)/news/(?P<pk>[\d+])/$', InstanceModelView.as_view(resource=NewsItemResource)),
    
)
