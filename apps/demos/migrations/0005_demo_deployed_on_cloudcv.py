# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-09 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0004_demo_from_origami'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='deployed_on_cloudcv',
            field=models.BooleanField(default=False),
        ),
    ]
