# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-12 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20180912_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
