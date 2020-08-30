"""Layout views."""

# Django REST Framework
from rest_framework import status, viewsets

# Serializers
from eventup.event_templates.serializers import LayoutCreateSerializer


from eventup.utils.interface.responses import CustomActions


class LayoutViewSet(viewsets.GenericViewSet):
    """ Layout view set

        Crud for layouts
    """

    def create(self, request, *args, **kwargs):
        """ Handle HTTP POST request """

        status_custom = False
        message = 'Error to create a new layout'
        serializer = LayoutCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        layout = serializer.save()

        if layout:
            status_custom = True
            message = "Layout created with success"

        return CustomActions().custom_response(status.HTTP_200_OK, status_custom, message)
