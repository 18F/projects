# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_is_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='business_unit',
            field=models.ForeignKey(blank=True, default=None, help_text='The Business Unit associated with the project', null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.BusinessUnit', verbose_name='Business Unit'),
        ),
    ]
