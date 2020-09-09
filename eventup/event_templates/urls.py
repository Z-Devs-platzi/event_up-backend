"""Users URLs."""

# Django
from django.urls import include, path

# Django Rest framework
from rest_framework.routers import DefaultRouter

# Views
from eventup.event_templates.views import template as template_views
from eventup.event_templates.views import layout as layout_views


router = DefaultRouter()
router.register(r'template', template_views.TemplateViewSet, basename='template')
router.register(r'layout', layout_views.LayoutViewSet, basename='event')
# router.register(r'users/verify/<str:code>/', user_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
