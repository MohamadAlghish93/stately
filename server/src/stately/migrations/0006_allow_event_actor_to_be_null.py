# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stately', '0005_add_related_names_for_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='actor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='stately.Actor'),
        ),
    ]
