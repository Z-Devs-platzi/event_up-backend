"""Expositors views."""

# Django REST Framework
from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404

# Model
from eventup.events.models import Expositor

# Serializers
from eventup.events.serializers import (
    ExpositorModelSerializer,
    CreateUpdateExpositorSerializer,
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


# class ExpositorViewSet(mixins.ListModelMixin,
#                        mixins.CreateModelMixin,
#                        mixins.RetrieveModelMixin,
#                        mixins.UpdateModelMixin,
#                        viewsets.GenericViewSet):
class ExpositorViewSet(
        CustomCreateModelMixin,
        CustomRetrieveModelMixin,
        CustomListModelMixin,
        CustomUpdateModelMixin,
        CustomDestroyModelMixin,
        viewsets.GenericViewSet):
    """Expositor view set.

       Crud for a expositors
    """
    custom_actions = CustomActions()
    queryset = Expositor.objects.all()
    serializer_class = ExpositorModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == ['create', 'update']:
            return CreateUpdateExpositorSerializer
        return ExpositorModelSerializer
