# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_auto_20171115_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='createtime',
            field=models.DateTimeField(default='2017-11-15 21:58:48'),
        ),
        migrations.AddField(
            model_name='skill',
            name='updatetime',
            field=models.DateTimeField(default='2017-11-15 21:58:48'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='createtime',
            field=models.DateTimeField(default='2017-11-15 21:58:48'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updatetime',
            field=models.DateTimeField(default='2017-11-15 21:58:48'),
        ),
    ]