""" Templates Admin """

# Django
from django.contrib import admin

# Models
from eventup.event_templates.models import Template


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    """ Template model admin """
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
