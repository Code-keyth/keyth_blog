# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0003_auto_20171114_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=255)),
                ('autor', models.IntegerField(max_length=11)),
                ('state', models.IntegerField(max_length=1)),
                ('clicks', models.IntegerField(max_length=6)),
                ('outline', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('label', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=254)),
                ('autor', models.IntegerField(max_length=11)),
                ('classify', models.IntegerField(max_length=11)),
                ('state', models.IntegerField(max_length=1)),
                ('clicks', models.IntegerField(max_length=6)),
                ('outline', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('true_name', models.CharField(max_length=20)),
                ('cookile', models.CharField(max_length=50)),
                ('is_root', models.IntegerField(max_length=2)),
                ('state', models.IntegerField(max_length=2)),
                ('loginip', models.CharField(max_length=20)),
                ('logintime', models.CharField(max_length=20)),
            ],
        ),
    ]