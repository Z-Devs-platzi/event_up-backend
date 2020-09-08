""" Layout Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.event_templates.models import Layout


class LayoutModelSerializer(serializers.ModelSerializer):
    """ Layout model serializer """

    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        """Meta class."""

        # fields = '__all__'
        model = Layout
        # read_only_fields
        fields = (
            'id',
            'comment'
        )

