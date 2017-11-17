# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20171115_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='updatetime',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='./static/admin/upload/'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='./static/admin/upload/'),
        ),
    ]