# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='date',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='hourly_rate',
        ),
        migrations.AddField(
            model_name='invoice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='paid',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]