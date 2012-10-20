from djangorestframework.resources import ModelResource
from service import models

class LocationResource(ModelResource):
    model = models.Location
    exclude = None
    
class AreaResource(ModelResource):
    model = models.Area
    exclude = None
    
class EventResource(ModelResource):
    model = models.Event
    exclude = None
    
class ActivityResource(ModelResource):
    model = models.Activity
    exclude = None
    
class NewsItemResource(ModelResource):
    model = models.NewsItem
    exclude = None
    