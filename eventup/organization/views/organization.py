"""Organization views."""

# Django REST Framework
from rest_framework import status, viewsets

# Serializers
from eventup.organization.serializers import OrganizationCreateSerializer


from eventup.utils.interface.responses import CustomActions


class OrganizationViewSet(viewsets.GenericViewSet):
    """ Organization view set

        Crud for template
    """

    def create(self, request, *args, **kwargs):
        """ Handle HTTP POST request """

        status_custom = False
        message = 'Error to create a new Organization'
        serializer = OrganizationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        organization = serializer.save()

        if organization:
            status_custom = True
            message = "Organization created with success"

        return CustomActions().custom_response(status.HTTP_200_OK, status_custom, message)
