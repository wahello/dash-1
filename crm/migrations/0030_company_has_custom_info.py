# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0029_auto_20170816_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='has_custom_info',
            field=models.BooleanField(default=False, editable=False, verbose_name='是否填写海关信息'),
        ),
    ]
