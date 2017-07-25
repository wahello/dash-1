# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_auto_20170725_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='individual_address',
        ),
        migrations.AddField(
            model_name='company',
            name='individual_bank',
            field=models.CharField(blank=True, max_length=255, verbose_name='基本户开户银行'),
        ),
    ]