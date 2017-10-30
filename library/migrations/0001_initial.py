# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 19:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0087_auto_20171015_0301'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_title', models.CharField(blank=True, editable=False, max_length=255, verbose_name='公司名称')),
                ('name', models.CharField(max_length=255, verbose_name='物品名')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='数量')),
                ('type', models.CharField(choices=[('营业执照正本', '营业执照正本'), ('营业执照副本', '营业执照副本'), ('金税盘', '金税盘'), ('发票领购本', '发票领购本'), ('公章', '公章'), ('发票章', '发票章'), ('财务章', '财务章'), ('私章', '私章'), ('公司章程', '公司章程'), ('扣款协议', '扣款协议'), ('开户许可证', '开户许可证'), ('机构信用代码证', '机构信用代码证'), ('身份证原件', '身份证原件'), ('开业通知书', '开业通知书'), ('变更通知书', '变更通知书'), ('账册', '账册'), ('凭证', '凭证'), ('租赁合同', '租赁合同'), ('汇缴报告', '汇缴报告'), ('其它', '其它')], default='身份证原件', max_length=100, verbose_name='类型')),
                ('status', models.CharField(choices=[('寄存', '寄存'), ('借出', '借出'), ('已归还', '已归还'), ('遗失', '遗失'), ('损坏', '损坏')], default='寄存', max_length=50, verbose_name='状态')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='归还日期')),
                ('received_at', models.DateTimeField(blank=True, null=True, verbose_name='签收日期')),
                ('status_updated', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='状态更新于')),
                ('note', models.CharField(blank=True, max_length=255, verbose_name='备注')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to=settings.AUTH_USER_MODEL, verbose_name='借用人')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Company', verbose_name='所属客户')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='签收者')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('action', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('type', models.CharField(choices=[('签收', '签收'), ('归还', '归还')], default='签收', max_length=50, verbose_name='类型')),
                ('items', models.TextField(blank=True, verbose_name='物品列表')),
                ('no', models.CharField(blank=True, max_length=200, verbose_name='收据编号')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Company', verbose_name='客户')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作员')),
            ],
        ),
    ]