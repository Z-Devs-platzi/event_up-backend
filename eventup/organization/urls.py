"""Organization URLs."""

# Django
from django.urls import include, path

# Django Rest framework
from rest_framework.routers import DefaultRouter

# Views
from eventup.organization.views import organization as organization_view

# Set Routers
router = DefaultRouter()
router.register(r'organization', organization_view.OrganizationViewSet, basename='organization')

urlpatterns = [
    path('', include(router.urls)),
]
