# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-28 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20171228_1422'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Application',
            new_name='Apply',
        ),
    ]