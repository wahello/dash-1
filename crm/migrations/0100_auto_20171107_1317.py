# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-07 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0099_auto_20171107_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='withhold_invoice',
            new_name='withholding',
        ),
    ]
