# Generated by Django 3.1 on 2020-08-30 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20200830_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='social_url',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]