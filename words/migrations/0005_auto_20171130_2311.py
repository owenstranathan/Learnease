# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_word_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='hsk_level',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default=1, max_length=1),
        ),
    ]