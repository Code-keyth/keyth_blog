# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_blog_createtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createtime',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updatetime',
            field=models.DateField(max_length=10),
        ),
    ]