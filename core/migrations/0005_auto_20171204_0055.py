# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-03 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tag_taggeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='colour',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
