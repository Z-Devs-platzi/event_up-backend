"""Organization views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins

# Serializers
from eventup.organization.serializers import OrganizationModelSerializer
from eventup.organization.models import Organization

# Permissions
from rest_framework.permissions import IsAuthenticated


class OrganizationViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """ Organization view set

        Crud for template
    """

    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""

        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
