""" Schedule views """

# Django REST Framework
from rest_framework import status, viewsets

# Serializers
from eventup.events.serializers import ScheduleCreateSerializer


from eventup.utils.interface.responses import CustomActions


class ScheduleViewSet(viewsets.GenericViewSet):
    """ Schedule view set

        Crud for schedule
     """

    def create(self, request, *args, **kwargs):
        """Handle HTTP POST request."""

        status_custom = False
        message = 'Error to create a new Schedule'
        serializer = ScheduleCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        expositor = serializer.save()

        if expositor:
            status_custom = True
            message = 'Schedule created with success'

        return CustomActions().custom_response(status.HTTP_200_OK, status_custom, message)

    # expositor/

    def get(self, request, *args, **kwargs):
        """Return Schedule."""

        # expositors = Expositor.objects.all()
        message = 'Schedule data'
        return CustomActions().custom_response(status.HTTP_200_OK, True, message)
