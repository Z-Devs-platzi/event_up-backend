"""Layout views."""

# Django REST Framework
from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404

# Model
from eventup.event_templates.serializers import Layout

# Serializers
from eventup.event_templates.serializers.layout import LayoutModelSerializer

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


class LayoutViewSet(
        CustomCreateModelMixin,
        CustomRetrieveModelMixin,
        CustomListModelMixin,
        CustomUpdateModelMixin,
        CustomDestroyModelMixin,
        viewsets.GenericViewSet):
    """ Layout view set

        Crud for layouts
    """
    custom_actions = CustomActions()
    queryset = Layout.objects.all()
    serializer_class = LayoutModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        return LayoutModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
