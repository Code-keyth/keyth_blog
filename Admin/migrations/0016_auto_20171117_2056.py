# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_auto_20171117_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createtime',
            field=models.DateTimeField(default='2017-11-17 20:56:30'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updatetime',
            field=models.DateTimeField(default='2017-11-17 20:56:30'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='time',
            field=models.DateTimeField(default='2017-11-17 20:56:30'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='createtime',
            field=models.DateTimeField(default='2017-11-17 20:56:30'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='updatetime',
            field=models.DateTimeField(default='2017-11-17 20:56:30'),
        ),
    ]
