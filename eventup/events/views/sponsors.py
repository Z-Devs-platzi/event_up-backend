"""Expositors views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins
# from rest_framework import request
# from rest_framework import generics


# Serializers
from eventup.events.serializers import SponsorModelSerializer
from eventup.events.models import Sponsor

# Permissions
from rest_framework.permissions import IsAuthenticated

# Complements
# from eventup.utils.interface.responses import CustomActions


class SponsorViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
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


# class UpdateSponsor(generics.UpdateAPIView):
#     queryset = Sponsor.objects.all()
#     serializer_class = SponsorModelSerializer
#     permission_classes = (IsAuthenticated,)

#     def update(self, instance, validated_data):

#         instance = self.get_object()

#         instance.name = request.data.get('name', instance.name)
#         instance.level = request.data.get('level', instance.level)
#         instance.web = request.data.get('web', instance.web)
#         instance.logo = request.data.get('logo', instance.logo)
#         instance.save()

#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return self.custom_actions.custom_response(instance)
