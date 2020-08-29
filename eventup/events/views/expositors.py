"""Expositors views."""

# Django REST Framework
from rest_framework import status, viewsets

# Serializers
from eventup.events.serializers import (
    ExpositorCreateSerializer,
)


from eventup.utils.interface.responses import CustomActions


class ExpositorViewSet(viewsets.GenericViewSet):
    """Expositor view set.

       Crud for a expositors
    """

    # expositor/create

    def create(self, request, *args, **kwargs):
        """Handle HTTP POST request."""

        status_custom = False
        message = 'Error to create a new Expositor'
        serializer = ExpositorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        expositor = serializer.save()

        if expositor:
            status_custom = True
            message = 'Expositor created with success'

        return CustomActions().custom_response(status.HTTP_200_OK, status_custom, message)

    # expositor/

    def get(self, request, *args, **kwargs):
        """Return Expositor."""

        # expositors = Expositor.objects.all()
        message = 'Expositors data'
        return CustomActions().custom_response(status.HTTP_200_OK, True, message)
