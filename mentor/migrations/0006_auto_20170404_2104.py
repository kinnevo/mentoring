# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0005_auto_20170403_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('facebook', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(blank=True, max_length=20)),
                ('mentor', models.CharField(blank=True, max_length=20)),
                ('mentee', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]