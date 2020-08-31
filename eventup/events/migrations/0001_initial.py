# Generated by Django 3.1 on 2020-08-31 02:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event_templates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expositor',
            fields=[
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('twitter', models.URLField(blank=True, max_length=255)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='expositors/pictures/', verbose_name='profile picture')),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('web', models.URLField(blank=True, max_length=300, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='sponsors/pictures/', verbose_name='sponsor logo')),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('expositors', models.ManyToManyField(to='events.Expositor')),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('banner_img', models.ImageField(blank=True, null=True, upload_to='banner/pictures/', verbose_name='banner picture')),
                ('banner_title', models.CharField(blank=True, max_length=300)),
                ('schedule', models.ManyToManyField(to='events.Schedule')),
                ('sponsor', models.ManyToManyField(to='events.Sponsor')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_templates.template')),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
