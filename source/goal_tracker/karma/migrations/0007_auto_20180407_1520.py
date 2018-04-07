# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 15:20
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karma', '0006_auto_20180407_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentongoal',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentonprogress',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentonproject',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentongoal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 19, 38, 236089)),
        ),
        migrations.AlterField(
            model_name='commentonprogress',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 19, 38, 237462)),
        ),
        migrations.AlterField(
            model_name='commentonproject',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 19, 38, 236826)),
        ),
        migrations.AlterField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 19, 38, 231981)),
        ),
        migrations.AlterField(
            model_name='progress',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 19, 38, 235512)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 19, 38, 234861)),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 19, 38, 230846)),
        ),
    ]