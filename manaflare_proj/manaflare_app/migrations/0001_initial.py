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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('hash_id', models.CharField(unique=True, verbose_name='Hash ID', max_length=50)),
                ('layout', models.IntegerField(choices=[(0, 'Normal'), (1, 'Split'), (2, 'Flip'), (3, 'Double Faced'), (4, 'Token'), (5, 'Plane'), (6, 'Scheme'), (7, 'Phenomenon'), (8, 'Leveler'), (9, 'Vanguard')], verbose_name='Layout')),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=75)),
                ('names', separatedvaluesfield.models.SeparatedValuesField(verbose_name='Names', max_length=150)),
                ('mana_cost', models.CharField(null=True, verbose_name='Mana Cost', max_length=20)),
                ('cmc', models.FloatField(null=True, default=0, verbose_name='Converted Mana Cost')),
                ('type', models.CharField(verbose_name='Card Type', max_length=100)),
                ('text', models.TextField(default='', verbose_name='Rules Text')),
                ('power', models.CharField(null=True, verbose_name='Power', max_length=5)),
                ('toughness', models.CharField(null=True, verbose_name='Toughness', max_length=5)),
                ('loyalty', models.IntegerField(null=True, verbose_name='Loyalty')),
                ('watermark', models.CharField(null=True, verbose_name='Watermark', max_length=20)),
                ('original_text', models.TextField(null=True, verbose_name='Original Text')),
                ('original_type', models.TextField(null=True, verbose_name='Original Type')),
            ],
        ),
        migrations.CreateModel(
            name='CardColors',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('color', models.IntegerField(choices=[(0, 'Red'), (1, 'Green'), (2, 'Blue'), (4, 'White'), (3, 'Black')], verbose_name='Color')),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='FormatRelationship',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'Legal'), (1, 'Banned'), (2, 'Restricted')], verbose_name='Legality')),
                ('card', models.ForeignKey(to='manaflare_app.Card')),
                ('format', models.ForeignKey(to='manaflare_app.Format')),
            ],
        ),
        migrations.CreateModel(
            name='Printing',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('rarity', models.IntegerField(choices=[(0, 'Common'), (1, 'Uncommon'), (2, 'Rare'), (3, 'Mythic Rare'), (4, 'Special'), (5, 'Basic Land')], verbose_name='Rarity')),
                ('flavor', models.TextField(null=True, verbose_name='Flavor Text')),
                ('number', models.CharField(null=True, verbose_name='Card Number', max_length=5)),
                ('multiverse_id', models.IntegerField(null=True, verbose_name='Multiverse Id')),
                ('variations', separatedvaluesfield.models.SeparatedValuesField(verbose_name='Variations', max_length=150)),
                ('border', models.CharField(null=True, verbose_name='Border Color', max_length=10)),
                ('timeshifted', models.BooleanField(default=False, verbose_name='Is Timeshifted')),
                ('artist', models.ForeignKey(to='manaflare_app.Artist')),
                ('card', models.ForeignKey(to='manaflare_app.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Rulings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('text', models.TextField(verbose_name='Text')),
                ('card', models.ForeignKey(to='manaflare_app.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
                ('code', models.CharField(verbose_name='Code', max_length=4)),
                ('border_color', models.CharField(verbose_name='Border Color', max_length=10)),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('type', models.IntegerField(choices=[(0, 'Core'), (1, 'Expansion'), (2, 'Reprint'), (3, 'Box'), (4, 'Un'), (5, 'From The Vault'), (6, 'Premium Deck'), (7, 'Duel Deck'), (8, 'Starter'), (9, 'Commander'), (10, 'Planechase'), (11, 'Archenemy'), (12, 'Promo'), (13, 'Vanguard'), (14, 'Masters')], verbose_name='Set Type')),
                ('block', models.CharField(null=True, verbose_name='Block', max_length=20)),
                ('cards', models.ManyToManyField(through='manaflare_app.Printing', to='manaflare_app.Card')),
            ],
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.CharField(unique=True, verbose_name='Value', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SuperType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.CharField(unique=True, verbose_name='Value', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
            name='cards',
            field=models.ManyToManyField(through='manaflare_app.FormatRelationship', to='manaflare_app.Card'),
        ),
        migrations.AddField(
            model_name='format',
            name='sets',
            field=models.ManyToManyField(to='manaflare_app.Set'),
        ),
        migrations.AddField(
            model_name='card',
            name='color_identity',
            field=models.ManyToManyField(to='manaflare_app.CardColors', related_name='color_identity', db_constraint='Color Identity'),
        ),
        migrations.AddField(
            model_name='card',
            name='colors',
            field=models.ManyToManyField(to='manaflare_app.CardColors', related_name='card_color', db_constraint='Colors'),
        ),
        migrations.AddField(
            model_name='card',
            name='subtypes',
            field=models.ManyToManyField(to='manaflare_app.SubType', blank=True),
        ),
        migrations.AddField(
            model_name='card',
            name='supertypes',
            field=models.ManyToManyField(to='manaflare_app.SuperType', blank=True),
        ),
        migrations.AddField(
            model_name='card',
            name='types',
            field=models.ManyToManyField(to='manaflare_app.Type'),
        ),
    ]
