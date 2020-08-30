"""Layout views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins

# Serializers
from eventup.event_templates.serializers import LayoutModelSerializer
from eventup.event_templates.serializers import Layout

# Permissions
from rest_framework.permissions import IsAuthenticated


class LayoutViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """ Layout view set

        Crud for layouts
    """

    queryset = Layout.objects.all()
    serializer_class = LayoutModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""

        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
