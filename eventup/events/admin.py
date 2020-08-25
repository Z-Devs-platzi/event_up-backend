''' Event models admin '''

# Django
from django.contrib import admin

# Models
from eventup.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ''' Event model admin '''

    list_display = ('name', 'date', 'hour', 'url')
    search_fields = ('name',)
    list_filter = ('name', 'date', 'hour')
