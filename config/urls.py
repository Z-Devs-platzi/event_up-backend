"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # API - Urls
    path('', include(('eventup.users.urls', 'users'), namespace='users')),
    path('', include(('eventup.events.urls', 'events'), namespace='events')),
    path('', include(('eventup.event_templates.urls', 'event_templates'), namespace='event_templates')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
