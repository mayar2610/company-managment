# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_structure', '0004_auto_20170705_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='parent_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
