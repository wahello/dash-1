# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 15:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0108_auto_20171212_0217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日期')),
                ('data', jsonfield.fields.JSONField(default='{}')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bookkeeper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='记账员')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Company', verbose_name='公司')),
            ],
            options={
                'verbose_name': '查账',
                'verbose_name_plural': '查账',
            },
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together=set([('company', 'date')]),
        ),
    ]
