# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20160601_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_billable',
            field=models.BooleanField(default=False, help_text='Whether or not the project is chargeable to a non-18F client.'),
        ),
    ]
