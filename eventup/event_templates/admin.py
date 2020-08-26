""" Templates Admin """

# Django
from django.contrib import admin

# Models
from eventup.event_templates.models import Template, Layout


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    """ Template model admin """
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):
    """ Layout model admin """
    list_display = ('pk', 'comment')
    search_fields = ('comment',)
    list_filter = ('comment',)
