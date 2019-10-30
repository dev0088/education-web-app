# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-30 15:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180720_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])])),
                ('isPublic', models.IntegerField(choices=[(0, 'Private'), (1, 'Public')], default=0)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_files', to='accounts.School')),
            ],
            options={
                'verbose_name': 'School File',
                'verbose_name_plural': 'School Files',
            },
        ),
    ]
