"""Expositors views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins

# Serializers
from eventup.events.serializers import SponsorModelSerializer
from eventup.events.models import Sponsor

# Permissions
from rest_framework.permissions import IsAuthenticated


class SponsorViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """ Sponsor view set

        Crud for sponsors
    """

    queryset = Sponsor.objects.all()
    serializer_class = SponsorModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""

        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
