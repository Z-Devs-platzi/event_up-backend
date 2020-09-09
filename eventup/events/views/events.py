"""Events views."""

# Django REST Framework
from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404

# Model
from eventup.events.models import Event

# Serializers
from eventup.events.serializers import (
    EventModelSerializer,
    CreateUpdateEventSerializer,
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


class EventViewSet(
        CustomCreateModelMixin,
        CustomRetrieveModelMixin,
        CustomListModelMixin,
        CustomUpdateModelMixin,
        CustomDestroyModelMixin,
        viewsets.GenericViewSet):
    """Event view set.

       Crud for a events
    """
    custom_actions = CustomActions()
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == ['create', 'update']:
            return CreateUpdateEventSerializer
        return EventModelSerializer
