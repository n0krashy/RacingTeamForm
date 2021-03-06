# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone', models.BigIntegerField(unique=True)),
                ('Age', models.PositiveSmallIntegerField(blank=True)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('Comment', models.TextField(blank=True)),
            ],
        ),
    ]
