from service.models import Location, Area, Event, Activity, NewsItem
from django.contrib import admin

class ActivityAdmin(admin.ModelAdmin):
    ordering = ('start_time', )
    list_display = ('name', 'start_time', 'end_time', 'area')

admin.site.register(Location)
admin.site.register(Area)
admin.site.register(Event)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(NewsItem)
