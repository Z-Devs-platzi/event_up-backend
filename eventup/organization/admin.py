''' Event models admin '''

# Django
from django.contrib import admin

# Models
from eventup.organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    ''' Organization model admin '''

    list_display = ('name', 'social_url')
    search_fields = ('name',)
    list_filter = ('name',)
