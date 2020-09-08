"""Template views."""

# Django REST Framework
from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404

# Model
from eventup.event_templates.serializers import Template

# Serializers
from eventup.event_templates.serializers.template import TemplateModelSerializer

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


class TemplateViewSet(
        CustomCreateModelMixin,
        CustomRetrieveModelMixin,
        CustomListModelMixin,
        CustomUpdateModelMixin,
        CustomDestroyModelMixin,
        viewsets.GenericViewSet):
    """ Template view set

        Crud for templates
    """
    custom_actions = CustomActions()
    queryset = Template.objects.all()
    serializer_class = TemplateModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        return TemplateModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
