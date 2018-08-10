# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-08 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEO', '0005_auto_20180808_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherAddress',
            fields=[
                ('id', models.AutoField(help_text='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('CoinCode', models.CharField(blank=True, help_text='币种', max_length=128, verbose_name='币种')),
                ('Myaddress', models.CharField(blank=True, default='', help_text='地址', max_length=256, verbose_name='地址')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('IsDelete', models.BooleanField(default=False, help_text='是否删除', verbose_name='是否删除')),
                ('IsUse', models.BooleanField(default=False, help_text='是否使用', verbose_name='是否使用')),
            ],
            options={
                'verbose_name': 'Other地址表',
                'db_table': 'other_address',
                'ordering': ['-create_time'],
            },
        ),
    ]
