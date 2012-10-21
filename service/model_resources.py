from djangorestframework.resources import ModelResource
from djangorestframework.reverse import reverse
from service import models

class LocationResource(ModelResource):
    model = models.Location
    fields = ['id', 'name', 'areas']
    
    def areas(self, instance):
        return reverse('areas',
                       kwargs={'location': instance.id}, 
                       request=self.request)
    
class AreaResource(ModelResource):
    model = models.Area
    fields = ['id', 'name', 'location']
    
    def location(self, instance):
        return reverse('location', 
                       kwargs={'pk': instance.location_id}, 
                       request=self.request)
    
class EventResource(ModelResource):
    model = models.Event
    fields = ['id', 'name', 'start_time', 'end_time', 'location', 'activities']
    
    def location(self, instance):
        return reverse('location', 
                       kwargs={'pk': instance.location_id},
                       request = self.request)
        
    def activities(self, instance):
        return reverse('activities', 
                       kwargs={'event': instance.id},
                       request=self.request)
    
class ActivityResource(ModelResource):
    model = models.Activity
    fields = ['id', 'name', 'start_time', 'end_time', 'area', 'news']
    
    def area(self, instance):
        return reverse('area', 
                       kwargs={'pk': instance.area_id},
                       request=self.request)
   
    def news(self, instance):
        return reverse('activity-news', 
                       kwargs={'activity': instance.id},
                       request=self.request)
    
class NewsItemResource(ModelResource):
    model = models.NewsItem
    fields = ['id', 'title', 'text', 'event', 'activity']
    
    def event(self, instance):
        return reverse('event',
                       kwargs={'pk': instance.event_id},
                       request=self.request)
    
    def activity(self, instance):
        if(instance.activity):
            return reverse('activity',
                       kwargs={'pk': instance.event_id},
                       request=self.request)
        else:
            return ""