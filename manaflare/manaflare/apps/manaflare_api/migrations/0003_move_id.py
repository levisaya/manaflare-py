# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manaflare_api', '0002_add_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='hash_id',
        ),
        migrations.AddField(
            model_name='printing',
            name='hash_id',
            field=models.CharField(unique=True, verbose_name='Hash ID', max_length=50, default=''),
            preserve_default=False,
        ),
    ]
