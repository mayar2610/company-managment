# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_structure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='company',
            name='parent_name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
