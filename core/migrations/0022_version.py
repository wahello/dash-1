# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-14 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20171209_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, max_length=100, verbose_name='version')),
                ('content', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
        ),
    ]
