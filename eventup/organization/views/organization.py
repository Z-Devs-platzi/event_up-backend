"""Organizations views."""

# Django REST Framework
from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404

# Model
from eventup.organization.models import Organization

# Serializers
from eventup.organization.serializers import (
    OrganizationModelSerializer,
    CreateUpdateOrganizationSerializer,
)

# Permissions
from rest_framework.permissions import IsAuthenticated

# Actions / Utils
from eventup.utils import (
    CustomCreateModelMixin,
    CustomRetrieveModelMixin,
    CustomListModelMixin,
    CustomUpdateModelMixin,
    CustomDestroyModelMixin
)
from eventup.utils.interface.responses import CustomActions


class OrganizationViewSet(
        CustomCreateModelMixin,
        CustomRetrieveModelMixin,
        CustomListModelMixin,
        CustomUpdateModelMixin,
        CustomDestroyModelMixin,
        viewsets.GenericViewSet):
    """Organization view set.

       Crud for a organizations
    """
    custom_actions = CustomActions()
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == ['create', 'update']:
            return CreateUpdateOrganizationSerializer
        return OrganizationModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
