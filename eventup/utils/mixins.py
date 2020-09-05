"""Mixins General."""

# Django REST Framework
from rest_framework import status

# Utils / Response
from eventup.utils.interface.responses import CustomActions

# Make Actions
custom_actions = CustomActions()


class CustomRetrieveModelMixin:
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        data = None
        try:
            instance = self.get_object()
        except Exception:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')

        if not data:
            # Get Object
            content = self.get_serializer(instance).data
            # Return Data
            data = custom_actions.set_response(status.HTTP_200_OK, 'Get information!', content)
        # Get Status
        return custom_actions.custom_response(data)


class CustomListModelMixin:
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        content = None
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            content = response.data
        else:
            serializer = self.get_serializer(queryset, many=True)
            content = serializer.data

        if content:
            data = custom_actions.set_response(status.HTTP_200_OK, 'Get information!', content)
        else:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')
        # Get Status
        return custom_actions.custom_response(data)
