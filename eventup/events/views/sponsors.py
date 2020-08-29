"""Expositors views."""

# Django REST Framework
from rest_framework import status, viewsets

# Serializers
from eventup.events.serializers import (
    SponsorCreateSerializer,
)


from eventup.utils.interface.responses import CustomActions


class SponsorViewSet(viewsets.GenericViewSet):
    """ Sponsor view set

        Crud for sponsors
    """
    # sponsor/create

    def create(self, request, *args, **kwargs):
        """ Handle HTTP POST request """

        status_custom = False
        message = 'Error to create a new Sponsor'
        serializer = SponsorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exceptio=True)
        sponsor = serializer.save()

        if sponsor:
            status_custom = True
            message = "Sponsor created with success"
        return CustomActions().custom_response(status.HTTP_200_OK, status_custom, message)

    def get(self, request, *args, **kwargs):
        """Return Sponsor."""

        message = 'Expositors data'
        return CustomActions().custom_response(status.HTTP_200_OK, True, message)
