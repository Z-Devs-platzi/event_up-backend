""" Template Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.event_templates.models import Template


class TemplateModelSerializer(serializers.ModelSerializer):
    """ Template model serializer """

    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        """Meta class."""

        # fields = '__all__'
        model = Template
        # read_only_fields
        fields = (
            'id',
            'comment'
        )

