"""Community views."""

# Django REST Framework
from rest_framework import status, viewsets

# Serializers
from eventup.communities.serializers import CommunityCreateSerializer


from eventup.utils.interface.responses import CustomActions


class CommunityViewSet(viewsets.GenericViewSet):
    """ Community view set

        Crud for template
    """

    def create(self, request, *args, **kwargs):
        """ Handle HTTP POST request """

        status_custom = False
        message = 'Error to create a new Community'
        serializer = CommunityCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        community = serializer.save()

        if community:
            status_custom = True
            message = "Community created with success"

        return CustomActions().custom_response(status.HTTP_200_OK, status_custom, message)
