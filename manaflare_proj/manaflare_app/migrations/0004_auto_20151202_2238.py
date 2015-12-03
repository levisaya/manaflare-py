# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manaflare_app', '0002_add_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='layout',
            field=models.IntegerField(verbose_name='Layout', choices=[(0, 'Normal'), (1, 'Split'), (2, 'Flip'), (3, 'Double Faced'), (4, 'Token'), (5, 'Plane'), (6, 'Scheme'), (7, 'Phenomenon'), (8, 'Leveler'), (9, 'Vanguard')]),
        ),
        migrations.AlterField(
            model_name='card',
            name='toughness',
            field=models.CharField(verbose_name='Toughness', default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='set',
            name='block',
            field=models.CharField(verbose_name='Block', null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='set',
            name='type',
            field=models.IntegerField(verbose_name='Set Type', choices=[(0, 'Core'), (1, 'Expansion'), (2, 'Reprint'), (3, 'Box'), (4, 'Un'), (5, 'From The Vault'), (6, 'Premium Deck'), (7, 'Duel Deck'), (8, 'Starter'), (9, 'Commander'), (10, 'Planechase'), (11, 'Archenemy'), (12, 'Promo'), (13, 'Vanguard'), (14, 'Masters')]),
        ),
    ]
