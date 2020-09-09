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
            'colors',
            'font',
            'layout'
        )


class CreateUpdateTemplateSerializer(TemplateModelSerializer):
    """Create template serializer."""

    colors = serializers.CharField(min_length=2, max_length=500)
    font = serializers.CharField(min_length=2, max_length=500)
    # Layout
    layout_id = serializers.CharField(min_length=2, max_length=100)

    def validate(self, data):
        """Verify passwords match."""
        # Check Template Name
        if 'layout' in data and Template.objects.filter(pk=data['layout']):
            raise serializers.ValidationError("The Id not exist.")
        else:
            data.update({'layout': Template.objects.get_by_id(data['layout'])})
            # del data['layout_id']

    def create(self, data):
        return Template.objects.create(**data)
