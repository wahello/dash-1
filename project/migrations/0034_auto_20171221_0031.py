# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0033_file_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('-created',), 'verbose_name': '文档', 'verbose_name_plural': '文档'},
        ),
    ]
