""" Template Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.event_templates.models import Template


class TemplateModelSerializer(serializers.HyperlinkedModelSerializer):
    """ Template model serializer """

    class Meta:
        """ Meta class """
        model = Template
        fields = (
            'id',
            'name',
            'colors',
            'banner',
            'font',
            'layout',
        )

    def validate(self, data):

        response = data
        return response

    def create(self, data):
        return Template.objects.create(**data)

    def update(self, instance, validated_data):
        template_validated_data = validated_data.pop('template', None)

        template = instance.template
        template.name = template_validated_data.get('name', template.name)
        template.colors = template_validated_data.get('colors', template.colors)
        template.banner = template_validated_data.get('banner', template.banner)
        template.font = template_validated_data.get('font', template.font)

        template.save()

        instance.save()
        return instance
