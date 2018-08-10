# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 17:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NEOAddress',
            fields=[
                ('id', models.AutoField(help_text='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('misc_desc', models.TextField(blank=True, default='', help_text='描述', verbose_name='描述')),
                ('status', models.IntegerField(choices=[(0, '有效'), (1, '无效'), (2, '待审核')], default=2, help_text='状态', verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('CoinCode', models.CharField(blank=True, default='BTC', help_text='币种', max_length=128, verbose_name='币种')),
                ('Myaddress', models.CharField(blank=True, default='', help_text='地址', max_length=256, verbose_name='地址')),
            ],
            options={
                'db_table': 'btcaddress',
                'ordering': ['-create_time'],
                'verbose_name': 'BTC地址表',
            },
        ),
        migrations.CreateModel(
            name='NEOBlockInfo',
            fields=[
                ('id', models.AutoField(help_text='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('misc_desc', models.TextField(blank=True, default='', help_text='描述', verbose_name='描述')),
                ('status', models.IntegerField(choices=[(0, '有效'), (1, '无效'), (2, '待审核')], default=2, help_text='状态', verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('CoinCode', models.CharField(blank=True, default='BTC', help_text='币种', max_length=128, verbose_name='币种')),
                ('BlockHash', models.CharField(blank=True, default='', help_text='区块哈希', max_length=256, verbose_name='区块哈希')),
                ('BlockNumber', models.IntegerField(blank=True, default=0, help_text='区块号', verbose_name='区块号')),
                ('BlockTime', models.IntegerField(blank=True, default=0, help_text='区块时间', verbose_name='区块时间')),
            ],
            options={
                'db_table': 'btcblockinfo',
                'ordering': ['-create_time'],
                'verbose_name': 'BTC区块已校验表',
            },
        ),
        migrations.CreateModel(
            name='NEOTransactions',
            fields=[
                ('id', models.AutoField(help_text='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('misc_desc', models.TextField(blank=True, default='', help_text='描述', verbose_name='描述')),
                ('status', models.IntegerField(choices=[(0, '有效'), (1, '无效'), (2, '待审核')], default=2, help_text='状态', verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('CoinCode', models.CharField(blank=True, default='BTC', help_text='币种', max_length=128, verbose_name='币种')),
                ('BlockHash', models.CharField(blank=True, default='', help_text='区块哈希', max_length=256, verbose_name='区块哈希')),
                ('BlockNumber', models.IntegerField(blank=True, default=0, help_text='区块号', verbose_name='区块号')),
                ('BlockTime', models.IntegerField(blank=True, default=0, help_text='区块时间', verbose_name='区块时间')),
                ('Tx_id', models.CharField(blank=True, default='', help_text='交易ID', max_length=256, verbose_name='交易ID')),
                ('Tx_time', models.IntegerField(blank=True, default=0, help_text='交易时间', verbose_name='交易时间')),
                ('Toaddress', models.CharField(blank=True, default='', help_text='收币方', max_length=256, verbose_name='收币方')),
                ('Fromaddress', models.CharField(blank=True, default='', help_text='打币方', max_length=256, verbose_name='打币方')),
                ('Amount', models.FloatField(blank=True, default=0, help_text='金额', max_length=96, verbose_name='金额')),
                ('Fee', models.FloatField(blank=True, default=0, help_text='小费', max_length=96, verbose_name='小费')),
                ('Used', models.BooleanField(default=False, help_text='是否已使用', verbose_name='是否已使用')),
                ('UserTime', models.DateField(default=datetime.date.today, help_text='访问时间', verbose_name='访问时间')),
            ],
            options={
                'db_table': 'btctransactions',
                'ordering': ['-create_time'],
                'verbose_name': 'BTC交易记录表',
            },
        ),
    ]
