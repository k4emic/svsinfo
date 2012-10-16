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

class Event(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.ForeignKey(Location)
    
    def __unicode__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event = models.ForeignKey(Event)
    area = models.ForeignKey(Area)
    
    def __unicode__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField();
    time = models.DateTimeField()
    event = models.ForeignKey(Event, null=True)
    activity = models.ForeignKey(Activity, null=True)
    
    def __unicode__(self):
        return self.title