""" Template Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.event_templates.models import Template


class TemplateModelSerializer(serializers.ModelSerializer):
    """ Template model serializer """

    class Meta:
        """ Meta class """
        model = Template
        fields = (
            'name',
            'colors',
            'banner',
            'font'
        )


class TemplateCreateSerializer(serializers.Serializer):
    """ Template create serializer """

    name = serializers.CharField()
    colors = serializers.CharField()
    banner = serializers.ImageField()
    font = serializers.CharField()

    def create(self, data):
        template = Template.objects.create(**data)

        return template
