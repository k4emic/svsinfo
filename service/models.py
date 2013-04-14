from django.db import models
import datetime

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
    
    class Meta:
        get_latest_by = 'start_time'
    
    @classmethod
    def current(cls):
        return cls.objects.all().latest()
    
    def dates(self):
        """
        Returns a list of all dates inclusive and between the start and end date of this convention
        """
        start_date = self.start_time.date()
        end_date = self.end_time.date()
        
        if(start_date > end_date):
            return []
        
        dates = []
        last_date = start_date
        
        while(last_date <= end_date):
            dates.append(last_date)
            last_date += datetime.timedelta(days=1)
            
        return dates
    
    def events_on_day(self, isoweekday):
        """
        Returns a queryset of events finding place on the specified isoweekday
        """
        weekday = isoweekday % 7 + 1
        events = self.event_set.filter(start_time__week_day=weekday).all()
        return events

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    convention = models.ForeignKey(Convention)
    area = models.ForeignKey(Area)
    
    class Meta:
        ordering = ('start_time', 'name')
    
    def __unicode__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField();
    time = models.DateTimeField(auto_now_add=True)
    
    convention = models.ForeignKey(Convention)
    event = models.ForeignKey(Event, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('-time',)
    