# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20170107_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel',
            old_name='date1',
            new_name='arrival',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='date2',
            new_name='departure',
        ),
        migrations.AlterField(
            model_name='birthday',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cooking',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='home',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personal',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='date',
            field=models.DateField(),
        ),
    ]
