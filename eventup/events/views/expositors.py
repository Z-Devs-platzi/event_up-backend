"""Expositors views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.generics import get_object_or_404

# Model
from eventup.events.models import Expositor

# Serializers
from eventup.events.serializers import (
    ExpositorModelSerializer,
    CreateExpositorSerializer,
)

# Permissions
from rest_framework.permissions import IsAuthenticated

# Actions / Utils
# from eventup.utils.interface.responses import CustomActions


class ExpositorViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """Expositor view set.

       Crud for a expositors
    """
    queryset = Expositor.objects.all()
    serializer_class = ExpositorModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    # def get_serializer_context(self):
    #     """Add expositor to serializer context."""
    #     context = super(ExpositorViewSet, self).get_serializer_context()
    #     context['expositor'] = self.expositor
    #     return context

    # # def dispatch(self, request, *args, **kwargs):
    # #     """Verify that the Expositor exists."""
    # #     print(request, args, kwargs)
    # #     # email = args['email']
    # #     # self.expositor = get_object_or_404(Expositor, email=email)
    # #     return super(ExpositorViewSet, self).dispatch(request, *args, **kwargs)

    # def get_serializer_class(self):
    #     """Return serializer based on action."""
    #     if self.action == 'create':
    #         return CreateExpositorSerializer
    #     return ExpositorModelSerializer

    # def get_queryset(self):
    #     """Restrict list to public-only."""
    #     if self.action == 'list':
    #         return self.queryset.filter(status='active')
    #     return self.queryset

    #     # """Return active circle's Expositors."""
    #     # if self.action not in ['finish', 'retrieve']:
    #     #     offset = timezone.now() + timedelta(minutes=10)
    #     #     return self.circle.Expositor_set.filter(
    #     #         departure_date__gte=offset,
    #     #         is_active=True,
    #     #         available_seats__gte=1
    #     #     )
    #     # return self.expositor.Expositor_set.all()
