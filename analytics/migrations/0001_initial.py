# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account_id', models.IntegerField()),
                ('summoner_id', models.IntegerField()),
                ('icon_id', models.IntegerField()),
                ('summoner_level', models.IntegerField()),
            ],
        ),
    ]