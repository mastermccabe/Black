# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-25 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeltReviewer', '0003_auto_20170925_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user_rating',
        ),
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
