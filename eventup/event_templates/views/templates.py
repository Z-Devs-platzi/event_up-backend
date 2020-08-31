"""Layout views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins

# Serializers
from eventup.event_templates.serializers import TemplateModelSerializer
from eventup.event_templates.models import Template


# Permissions
from rest_framework.permissions import IsAuthenticated


class TemplateViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """ Template view set

        Crud for templates
     """

    queryset = Template.objects.all()
    serializer_class = TemplateModelSerializer

    # def create(self, request):

    def get_permissions(self):
        """Assign permission based on action."""

        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
