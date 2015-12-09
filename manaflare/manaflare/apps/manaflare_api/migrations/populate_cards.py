# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from manaflare.apps.manaflare_api.populate import populate_from_json


class Migration(migrations.Migration):
    def forwards_func(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        populate_from_json(db_alias, ['ISD', 'BFZ'])

    def reverse_func(apps, schema_editor):
        db_alias = schema_editor.connection.alias

    dependencies = [
        ('manaflare_api', '0002_add_colors'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
