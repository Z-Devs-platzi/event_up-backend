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

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        # if self.action in ['update', 'partial_update', 'finish']:
        #     permissions.append(IsRideOwner)
        # if self.action == 'join':
        #     permissions.append(IsNotRideOwner)
        return [p() for p in permissions]
    # expositor/create

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset


    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        # if self.action in ['update', 'partial_update']:
        #     permissions.append(IsCircleAdmin)
        return [permission() for permission in permissions]
    # def create(self, request, *args, **kwargs):
    #     """Handle HTTP POST request."""
    #     # Make Serializer and Set Data
    #     serializer = ExpositorModelSerializer().create(data=request.data)
    #     # Validate Model
    #     if not serializer.is_valid():
    #         data = self.custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Error to create a new Expositor', serializer.errors)
    #     else:
    #         # Save Objectserializer
    #         expositor = serializer.save()
    #         # Return User
    #         content = {"email": expositor}
    #         data = self.custom_actions.set_response(status.HTTP_201_CREATED, 'Expositor created with success!', content)
    #     return self.custom_actions.custom_response(data)

    # # expositor/

    # def get(self, request, *args, **kwargs):
    #     """Return Expositor."""

    #     # expositors = Expositor.objects.all()
    #     message = 'Expositors data'
    #     return CustomActions().custom_response(status.HTTP_200_OK, True, message)
