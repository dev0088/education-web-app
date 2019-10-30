# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0011_fieldtrip_expected_head_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldtrip',
            name='name',
            field=models.CharField(blank=True, help_text='Not required, used interally (Parents and Teachers do not see this).', max_length=140),
        ),
    ]
