from service.models import Location, Area, Convention, Event, NewsItem
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    ordering = ('start_time', )
    list_display = ('name', 'start_time', 'end_time', 'area')

admin.site.register(Location)
admin.site.register(Area)
admin.site.register(Convention)
admin.site.register(Event, EventAdmin)
admin.site.register(NewsItem)
