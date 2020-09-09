""" Templates Admin """

# Django
from django.contrib import admin

# Models
from eventup.event_templates.models import Template, Layout


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    """ Template model admin """
    list_display = ('colors',)
    search_fields = ('colors',)
    list_filter = ('colors',)


@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):
    """ Layout model admin """
    list_display = ('id', 'comment')
    search_fields = ('comment',)
    list_filter = ('comment',)
