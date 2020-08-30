""" Schedule views """

# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins

# Serializers
from eventup.events.serializers import ScheduleModelSerializer
from eventup.events.models import Schedule

# Permissions
from rest_framework.permissions import IsAuthenticated


class ScheduleViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """ Schedule view set

        Crud for schedule
     """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""

        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Restrict list to public-only."""

        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
