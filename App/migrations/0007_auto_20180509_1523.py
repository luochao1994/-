# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20180509_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userticketmodel',
            name='creat_time',
            field=models.DateTimeField(null=True),
        ),
    ]
