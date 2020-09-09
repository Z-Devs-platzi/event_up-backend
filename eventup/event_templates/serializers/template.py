""" Template Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.event_templates.models import Template, Layout

# Serializers
from eventup.event_templates.serializers.layout import LayoutModelSerializer

class TemplateModelSerializer(serializers.ModelSerializer):
    """ Template model serializer """
    id = serializers.CharField(source='pk', read_only=True)
    layout = LayoutModelSerializer(read_only=True)

    class Meta:
        """Meta class."""

        model = Template
        # read_only_fields
        fields = (
            'id',
            'colors',
            'font',
            'layout',
            'layout_id'
        )


class CreateUpdateTemplateSerializer(TemplateModelSerializer):
    """Create template serializer."""

    colors = serializers.CharField(min_length=2, max_length=500)
    font = serializers.CharField(min_length=2, max_length=500)
    # Layout
    layout_id = serializers.CharField(min_length=1, max_length=100)

    def validate(self, data):
        """Verify information."""
        try:
            self.context['layout'] = Layout.objects.get(id=data['layout_id'])
        except Layout.DoesNotExist:
            raise serializers.ValidationError("The Id not exist.")
        del data['layout_id']
        return data

    def create(self, data):
        return Template.objects.create(**data, layout=self.context['layout'])
