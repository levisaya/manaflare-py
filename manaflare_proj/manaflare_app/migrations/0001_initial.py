# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import manaflare_app.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash_id', models.CharField(unique=True, verbose_name='Hash ID', max_length=50)),
                ('layout', models.IntegerField(choices=[(0, 'Normal'), (1, 'Split'), (2, 'Flip'), (3, 'DoubleFaced'), (4, 'Token'), (5, 'Plane'), (6, 'Scheme'), (7, 'Phenomenon'), (8, 'Leveler'), (9, 'Vanguard')], verbose_name='Layout')),
                ('name', models.CharField(verbose_name='Name', max_length=75)),
                ('names', manaflare_app.models.SeparatedValuesField(verbose_name='Names')),
                ('mana_cost', models.CharField(verbose_name='Mana Cost', max_length=20)),
                ('cmc', models.FloatField(verbose_name='Converted Mana Cost', default=0)),
                ('type', models.CharField(verbose_name='Card Type', max_length=100)),
                ('text', models.TextField(verbose_name='Rules Text', default='')),
                ('power', models.CharField(verbose_name='Power', max_length=5, default='')),
                ('toughness', models.CharField(verbose_name='Power', max_length=5, default='')),
                ('loyalty', models.IntegerField(verbose_name='Loyalty', null=True)),
                ('watermark', models.CharField(verbose_name='Watermark', max_length=20, default='')),
                ('original_text', models.TextField(verbose_name='Original Text')),
                ('original_type', models.TextField(verbose_name='Original Type')),
            ],
        ),
        migrations.CreateModel(
            name='CardColors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.IntegerField(choices=[(0, 'Red'), (1, 'Green'), (2, 'Blue'), (4, 'White'), (3, 'Black')], verbose_name='Color')),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Printing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rarity', models.IntegerField(choices=[(0, 'Common'), (1, 'Uncommon'), (2, 'Rare'), (3, 'Mythic Rare'), (4, 'Special'), (5, 'BasicLand')], verbose_name='Rarity')),
                ('flavor', models.TextField(verbose_name='Flavor Text')),
                ('number', models.CharField(verbose_name='Card Number', max_length=5)),
                ('multiverse_id', models.IntegerField(verbose_name='Multiverse Id')),
                ('variations', manaflare_app.models.SeparatedValuesField(verbose_name='Variations')),
                ('border', models.CharField(verbose_name='Border Color', max_length=10)),
                ('timeshifted', models.BooleanField(verbose_name='Is Timeshifted')),
                ('artist', models.ForeignKey(to='manaflare_app.Artist')),
                ('card', models.ForeignKey(to='manaflare_app.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Rulings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('text', models.TextField(verbose_name='Text')),
                ('card', models.ForeignKey(to='manaflare_app.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
                ('code', models.CharField(verbose_name='Code', max_length=4)),
                ('border_color', models.CharField(verbose_name='Border Color', max_length=10)),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('type', models.IntegerField(choices=[(0, 'Core'), (1, 'Expansion'), (2, 'Reprint'), (3, 'Box'), (4, 'Un'), (5, 'FromTheVault'), (6, 'PremiumDeck'), (7, 'DuelDeck'), (8, 'Starter'), (9, 'Commander'), (10, 'Planechase'), (11, 'Archenemy'), (12, 'Promo'), (13, 'Vanguard'), (14, 'Masters')], verbose_name='Set Type')),
                ('block', models.CharField(verbose_name='Block', max_length=20)),
                ('cards', models.ManyToManyField(through='manaflare_app.Printing', to='manaflare_app.Card')),
            ],
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, verbose_name='Value', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SuperType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, verbose_name='Value', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, verbose_name='Value', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='printing',
            name='set',
            field=models.ForeignKey(to='manaflare_app.Set'),
        ),
        migrations.AddField(
            model_name='format',
            name='sets',
            field=models.ManyToManyField(to='manaflare_app.Set'),
        ),
        migrations.AddField(
            model_name='card',
            name='color_identity',
            field=models.ManyToManyField(to='manaflare_app.CardColors', db_constraint='Color Identity', related_name='color_identity'),
        ),
        migrations.AddField(
            model_name='card',
            name='colors',
            field=models.ManyToManyField(to='manaflare_app.CardColors', db_constraint='Colors', related_name='card_color'),
        ),
        migrations.AddField(
            model_name='card',
            name='subtypes',
            field=models.ManyToManyField(blank=True, to='manaflare_app.SubType'),
        ),
        migrations.AddField(
            model_name='card',
            name='supertypes',
            field=models.ManyToManyField(blank=True, to='manaflare_app.SuperType'),
        ),
        migrations.AddField(
            model_name='card',
            name='types',
            field=models.ManyToManyField(to='manaflare_app.Type'),
        ),
    ]
