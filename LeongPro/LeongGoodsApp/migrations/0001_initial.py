# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('g_title', models.CharField(max_length=20)),
                ('g_pic', models.ImageField(upload_to='/static/media/')),
                ('iaDelete', models.BooleanField(default=False)),
                ('g_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('g_click', models.IntegerField(default=0)),
                ('g_unit', models.IntegerField(default='500')),
                ('g_jianji', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 15, 3, 15, 13, 924787))),
                ('pubg_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('t_title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(to='LeongGoodsApp.TypeInfo'),
        ),
    ]
