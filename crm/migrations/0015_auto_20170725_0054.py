# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20170725_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareholder',
            name='company_title',
            field=models.CharField(blank=True, editable=False, max_length=255, verbose_name='公司名'),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='people_name',
            field=models.CharField(blank=True, editable=False, max_length=200, verbose_name='姓名'),
        ),
    ]