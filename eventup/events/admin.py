''' Event models admin '''

# Django
from django.contrib import admin

# Models
from eventup.events.models import Event
from eventup.events.models import Sponsor


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
