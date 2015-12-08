# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from manaflare.apps.manaflare_api.v1.models import CardColors


def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    color_values = [color_enum[0] for color_enum in CardColors.COLORS]
    CardColors.objects.using(db_alias).bulk_create([CardColors(color=color_choice) for color_choice in color_values])


def reverse_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    color_values = [color_enum[0] for color_enum in CardColors.COLORS]

    for color_value in color_values:
        CardColors.objects.using(db_alias).filter(color=color_value).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('manaflare_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
