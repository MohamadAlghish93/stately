# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields

"""
New workflow definition format is:

context:
  <global context for handlers>

name: ...
states:
  - name: Not started
    actions:
      - name: ...
        template:
          <JSON-schema definition, or HTML snippet>
        handler: |
          <Python handler code>

Notable changes are that:
* template moved from the state to individual actions
* there's now global context for handlers
"""


def delete_all_workflows(apps, schema):
    Workflow = apps.get_model('stately', 'Workflow')
    Workflow.objects.all().delete()
    
    
class Migration(migrations.Migration):

    dependencies = [
        ('stately', '0002_alter_uniqueness_constraints'),
    ]

    operations = [
        migrations.RunPython(
            delete_all_workflows
        ),
        migrations.RemoveField(
            model_name='state',
            name='initial',
        ),
        migrations.RemoveField(
            model_name='state',
            name='template_func',
        ),
        migrations.AddField(
            model_name='action',
            name='template',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='workflow',
            name='context',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='action',
            name='handler',
            field=models.TextField(default=''),
        ),
    ]