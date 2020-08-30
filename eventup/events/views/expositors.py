"""Expositors views."""

# Django REST Framework
# from rest_framework import status, viewsets
from rest_framework import viewsets
from rest_framework import mixins

# Serializers
from eventup.events.serializers import ExpositorModelSerializer
from eventup.events.models import Expositor

# Permissions
from rest_framework.permissions import IsAuthenticated
# from cride.circles.permissions.me-mberships import IsActiveCircleMember
# from cride.rides.permissions.rides import IsRideOwner, IsNotRideOwner


# from eventup.utils.interface.responses import CustomActions


class ExpositorViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """Expositor view set.

       Crud for a expositors
    """
    queryset = Expositor.objects.all()
    serializer_class = ExpositorModelSerializer

    def get_permissions(self): # noqa
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        # if self.action in ['update', 'partial_update', 'finish']:
        #     permissions.append(IsRideOwner)
        # if self.action == 'join':
        #     permissions.append(IsNotRideOwner)
        return [permission() for permission in permissions]
    # expositor/create

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
