# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import separatedvaluesfield.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('layout', models.IntegerField(choices=[(0, 'Normal'), (1, 'Split'), (2, 'Flip'), (3, 'Double Faced'), (4, 'Token'), (5, 'Plane'), (6, 'Scheme'), (7, 'Phenomenon'), (8, 'Leveler'), (9, 'Vanguard')], verbose_name='Layout')),
                ('name', models.CharField(max_length=75, verbose_name='Name', unique=True)),
                ('names', separatedvaluesfield.models.SeparatedValuesField(max_length=150, verbose_name='Names')),
                ('mana_cost', models.CharField(max_length=20, verbose_name='Mana Cost', null=True)),
                ('cmc', models.FloatField(verbose_name='Converted Mana Cost', default=0, null=True)),
                ('type', models.CharField(max_length=100, verbose_name='Card Type')),
                ('text', models.TextField(verbose_name='Rules Text', default='')),
                ('power', models.CharField(max_length=5, verbose_name='Power', null=True)),
                ('toughness', models.CharField(max_length=5, verbose_name='Toughness', null=True)),
                ('loyalty', models.IntegerField(verbose_name='Loyalty', null=True)),
                ('watermark', models.CharField(max_length=20, verbose_name='Watermark', null=True)),
                ('original_text', models.TextField(verbose_name='Original Text', null=True)),
                ('original_type', models.TextField(verbose_name='Original Type', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('color', models.IntegerField(choices=[(0, 'R'), (1, 'G'), (2, 'U'), (3, 'B'), (4, 'W')], verbose_name='Color')),
            ],
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.CharField(max_length=100, verbose_name='Value', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=25, verbose_name='Name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormatRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'Legal'), (1, 'Banned'), (2, 'Restricted')], verbose_name='Legality')),
                ('card', models.ForeignKey(to='manaflare_api.Card')),
                ('format', models.ForeignKey(to='manaflare_api.Format')),
            ],
        ),
        migrations.CreateModel(
            name='Printing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('hash_id', models.CharField(max_length=50, verbose_name='Hash ID', unique=True)),
                ('rarity', models.IntegerField(choices=[(0, 'Common'), (1, 'Uncommon'), (2, 'Rare'), (3, 'Mythic Rare'), (4, 'Special'), (5, 'Basic Land')], verbose_name='Rarity')),
                ('flavor', models.TextField(verbose_name='Flavor Text', null=True)),
                ('number', models.CharField(max_length=5, verbose_name='Card Number', null=True)),
                ('multiverse_id', models.IntegerField(verbose_name='Multiverse Id', null=True)),
                ('variations', separatedvaluesfield.models.SeparatedValuesField(max_length=150, verbose_name='Variations')),
                ('border', models.CharField(max_length=10, verbose_name='Border Color', null=True)),
                ('timeshifted', models.BooleanField(verbose_name='Is Timeshifted', default=False)),
                ('artist', models.ForeignKey(to='manaflare_api.Artist')),
                ('card', models.ForeignKey(to='manaflare_api.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Rulings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('text', models.TextField(verbose_name='Text')),
                ('card', models.ForeignKey(to='manaflare_api.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('code', models.CharField(max_length=4, verbose_name='Code')),
                ('border_color', models.CharField(max_length=10, verbose_name='Border Color')),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('type', models.IntegerField(choices=[(0, 'Core'), (1, 'Expansion'), (2, 'Reprint'), (3, 'Box'), (4, 'Un'), (5, 'From The Vault'), (6, 'Premium Deck'), (7, 'Duel Deck'), (8, 'Starter'), (9, 'Commander'), (10, 'Planechase'), (11, 'Archenemy'), (12, 'Promo'), (13, 'Vanguard'), (14, 'Masters'), (15, 'Conspiracy')], verbose_name='Set Type')),
                ('block', models.CharField(max_length=20, verbose_name='Block', null=True)),
                ('cards', models.ManyToManyField(to='manaflare_api.Card', through='manaflare_api.Printing')),
            ],
        ),
        migrations.CreateModel(
            name='TypeLinkage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('supertype', models.BooleanField(default=False)),
                ('subtype', models.BooleanField(default=False)),
                ('card', models.ForeignKey(to='manaflare_api.Card')),
                ('type', models.ForeignKey(to='manaflare_api.CardType')),
            ],
        ),
        migrations.AddField(
            model_name='printing',
            name='set',
            field=models.ForeignKey(to='manaflare_api.Set'),
        ),
        migrations.AddField(
            model_name='format',
            name='cards',
            field=models.ManyToManyField(to='manaflare_api.Card', through='manaflare_api.FormatRelationship'),
        ),
        migrations.AddField(
            model_name='format',
            name='sets',
            field=models.ManyToManyField(to='manaflare_api.Set'),
        ),
        migrations.AddField(
            model_name='card',
            name='color_identity',
            field=models.ManyToManyField(db_constraint='Color Identity', related_name='color_identity', to='manaflare_api.CardColors'),
        ),
        migrations.AddField(
            model_name='card',
            name='colors',
            field=models.ManyToManyField(db_constraint='Colors', related_name='card_color', to='manaflare_api.CardColors'),
        ),
        migrations.AddField(
            model_name='card',
            name='types',
            field=models.ManyToManyField(to='manaflare_api.CardType', through='manaflare_api.TypeLinkage'),
        ),
    ]
