# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-09 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_structure', '0013_auto_20170706_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='total',
            field=models.IntegerField(default=None),
        ),
    ]