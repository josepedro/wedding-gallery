# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-17 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_photo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='status',
            field=models.CharField(default=b'Approve', max_length=10),
        ),
    ]
