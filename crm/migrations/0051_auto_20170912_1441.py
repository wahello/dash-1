# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0050_auto_20170912_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contactor',
            field=models.CharField(blank=True, max_length=255, verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='company',
            name='contactor_phone',
            field=models.CharField(blank=True, max_length=255, verbose_name='联系电话'),
        ),
    ]