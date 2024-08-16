from django.contrib import admin
from .models import RoadSegment

@admin.register(RoadSegment)
class RoadSegmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'long_start', 'lat_start', 'long_end', 'lat_end', 'length', 'speed', 'intensity')
    search_fields = ('long_start', 'lat_start', 'long_end', 'lat_end', 'length', 'speed')
   
    list_filter = ('speed',)
