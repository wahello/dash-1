# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0058_auto_20170913_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='note',
            field=models.CharField(blank=True, max_length=255, verbose_name='备注'),
        ),
    ]
