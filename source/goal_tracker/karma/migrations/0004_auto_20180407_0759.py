# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 07:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karma', '0003_user_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentongoal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 7, 59, 3, 35312)),
        ),
        migrations.AlterField(
            model_name='commentonprogress',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 7, 59, 3, 36428)),
        ),
        migrations.AlterField(
            model_name='commentonproject',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 7, 59, 3, 35861)),
        ),
        migrations.AlterField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 7, 59, 3, 32897)),
        ),
        migrations.AlterField(
            model_name='progress',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 7, 59, 3, 34620)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 7, 59, 3, 34037)),
        ),
    ]
