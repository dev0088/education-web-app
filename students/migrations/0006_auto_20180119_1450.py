# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20180119_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
