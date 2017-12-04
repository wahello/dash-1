# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import project.models.project


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20171129_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=project.models.project.get_logo_upload_path),
        ),
    ]