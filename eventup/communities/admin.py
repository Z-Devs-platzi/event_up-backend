''' Event models admin '''

# Django
from django.contrib import admin

# Models
from eventup.communities.models import Community


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    ''' Event model admin '''

    list_display = ('name', 'social_url')
    search_fields = ('name',)
    list_filter = ('name',)
