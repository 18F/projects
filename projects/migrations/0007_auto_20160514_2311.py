# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160512_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='active',
        ),
        migrations.AddField(
            model_name='project',
            name='project_lead',
            field=models.CharField(blank=True, help_text='Name of 18F employee who is responsible for this project.', max_length=255, verbose_name='Project Lead'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[(0, 'Tentative'), (1, 'Active'), (2, 'Paused'), (3, 'Complete')], default=1, help_text='Current status of the project.', max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='agency',
            field=models.CharField(blank=True, help_text='Agency is the level below the Department.', max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='cgac_agency_code',
            field=models.CharField(blank=True, max_length=255, verbose_name='CGAC Agency Code'),
        ),
        migrations.AlterField(
            model_name='client',
            name='department',
            field=models.CharField(blank=True, help_text='Deparment is the highest organizational level.', max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='omb_agency_code',
            field=models.CharField(blank=True, help_text='OMB Agency Code is the top level code.', max_length=255, verbose_name='OMB Agency Code'),
        ),
        migrations.AlterField(
            model_name='client',
            name='omb_bureau_code',
            field=models.CharField(blank=True, help_text='OMB Bureau Code is the level below OMB Agency Code.', max_length=255, verbose_name='OMB Bureau Code'),
        ),
        migrations.AlterField(
            model_name='client',
            name='treasury_agency_code',
            field=models.CharField(blank=True, max_length=255, verbose_name='Treasury Agency Code'),
        ),
        migrations.AlterField(
            model_name='project',
            name='billable',
            field=models.CharField(choices=[(0, 'Billable'), (1, 'Non-billable')], default=1, help_text='Whether or not the project is chargeable to a non-18F client.', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='cloud_dot_gov',
            field=models.BooleanField(default=False, help_text='Whether or not the project includes cloud.gov platform support.', verbose_name='Cloud.gov Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_url',
            field=models.URLField(blank=True, help_text='The GitHub URL of the project, e.g. https://github.com/18f/agile-bpa', verbose_name='GitHub URL'),
        ),
        migrations.AlterField(
            model_name='project',
            name='live_site_url',
            field=models.URLField(blank=True, help_text='A URL to the site where the project is deployed, if one exists.', verbose_name='Live URL'),
        ),
        migrations.AlterField(
            model_name='project',
            name='mb_number',
            field=models.CharField(blank=True, help_text='The unique identifier for an agreement inthe GSA financial system. This is different thanthe Tock ID.', max_length=100, verbose_name='MB Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tock_id',
            field=models.IntegerField(blank=True, help_text='The ID of the project in Tock.', null=True, unique=True, verbose_name='Tock ID'),
        ),
    ]
