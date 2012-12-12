from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class Area(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location)
    
    def __unicode__(self):
        return self.name

class Convention(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.ForeignKey(Location)
    
    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    convention = models.ForeignKey(Convention)
    area = models.ForeignKey(Area)
    
    def __unicode__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField();
    time = models.DateTimeField()
    
    convention = models.ForeignKey(Convention, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    