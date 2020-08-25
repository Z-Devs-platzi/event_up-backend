''' Event models admin '''

# Django
from django.contrib import admin

# Models
from eventup.events.models import Event, Sponsor, Expositor, Schedule


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ''' Event model admin '''

    list_display = ('name', 'date', 'hour', 'url')
    search_fields = ('name',)
    list_filter = ('name', 'date', 'hour')


@admin.register(Sponsor)
class SponsorsAdmin(admin.ModelAdmin):
    ''' Sponsors model admin '''

    list_display = ('name', 'level')
    search_fields = ('name',)
    list_filter = ('level',)


@admin.register(Expositor)
class ExpositorAdmin(admin.ModelAdmin):
    ''' Expositor model admin '''
    list_display = ('first_name', 'last_name', 'twitter')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    ''' Schedule model admin '''
    list_display = ('date',)
