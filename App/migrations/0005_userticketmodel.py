# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20180507_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTicketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=30)),
                ('creat_time', models.DateTimeField()),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.UserModel')),
            ],
            options={
                'db_table': 'user_ticket',
            },
        ),
    ]
