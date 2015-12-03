from django.db import models
from enum import Enum


class SuperType(models.Model):
    value = models.CharField('Value', max_length=100, unique=True)

    def __str__(self):
        return self.value


class Type(models.Model):
    value = models.CharField('Value', max_length=100, unique=True)

    def __str__(self):
        return self.value


class SubType(models.Model):
    value = models.CharField('Value', max_length=100, unique=True)

    def __str__(self):
        return self.value


class Artist(models.Model):
    name = models.CharField('Name', max_length=100, unique=True)


class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([s for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class CardColors(models.Model):
    COLOR_RED = 0
    COLOR_GREEN = 1
    COLOR_BLUE = 2
    COLOR_BLACK = 3
    COLOR_WHITE = 4

    COLORS = (
        (COLOR_RED, 'Red'),
        (COLOR_GREEN, 'Green'),
        (COLOR_BLUE, 'Blue'),
        (COLOR_WHITE, 'White'),
        (COLOR_BLACK, 'Black'),
    )

    color = models.IntegerField('Color', choices=COLORS)

    def __str__(self):
        return self.color


class Printing(models.Model):
    RARITY_COMMON = 0
    RARITY_UNCOMMON = 1
    RARITY_RARE = 2
    RARITY_MYTHIC = 3
    RARITY_SPECIAL = 4
    RARITY_BASIC_LAND = 5

    RARITIES = (
        (RARITY_COMMON, 'Common'),
        (RARITY_UNCOMMON, 'Uncommon'),
        (RARITY_RARE, 'Rare'),
        (RARITY_MYTHIC, 'Mythic Rare'),
        (RARITY_SPECIAL, 'Special'),
        (RARITY_BASIC_LAND, 'BasicLand')
    )

    rarity = models.IntegerField('Rarity', choices=RARITIES)
    flavor = models.TextField('Flavor Text')
    artist = models.ForeignKey('Artist')
    number = models.CharField('Card Number', max_length=5)
    multiverse_id = models.IntegerField('Multiverse Id')
    variations = SeparatedValuesField('Variations')
    border = models.CharField('Border Color', max_length=10)
    timeshifted = models.BooleanField('Is Timeshifted')

    card = models.ForeignKey('Card')
    set = models.ForeignKey('Set')


class Card(models.Model):
    LAYOUT_NORMAL = 0
    LAYOUT_SPLIT = 1
    LAYOUT_FLIP = 2
    LAYOUT_DOUBLE_FACED = 3
    LAYOUT_TOKEN = 4
    LAYOUT_PLANE = 5
    LAYOUT_SCHEME = 6
    LAYOUT_PHENOMENON = 7
    LAYOUT_LEVELER = 8
    LAYOUT_VANGUARD = 9


    LAYOUTS = (
        (LAYOUT_NORMAL, 'Normal'),
        (LAYOUT_SPLIT, 'Split'),
        (LAYOUT_FLIP, 'Flip'),
        (LAYOUT_DOUBLE_FACED, 'Double Faced'),
        (LAYOUT_TOKEN, 'Token'),
        (LAYOUT_PLANE, 'Plane'),
        (LAYOUT_SCHEME, 'Scheme'),
        (LAYOUT_PHENOMENON, 'Phenomenon'),
        (LAYOUT_LEVELER, 'Leveler'),
        (LAYOUT_VANGUARD, 'Vanguard')
    )

    hash_id = models.CharField('Hash ID', unique=True, max_length=50)
    layout = models.IntegerField('Layout', choices=LAYOUTS)
    name = models.CharField('Name', max_length=75)
    names = SeparatedValuesField('Names')
    mana_cost = models.CharField('Mana Cost', max_length=20)
    cmc = models.FloatField('Converted Mana Cost', default=0)
    colors = models.ManyToManyField(CardColors, 'Colors', related_name='card_color')
    color_identity = models.ManyToManyField(CardColors, 'Color Identity', related_name='color_identity')
    type = models.CharField('Card Type', max_length=100)
    supertypes = models.ManyToManyField('SuperType', blank=True)
    types = models.ManyToManyField('Type')
    subtypes = models.ManyToManyField('Subtype', blank=True)
    text = models.TextField('Rules Text', default='')
    power = models.CharField('Power', default='', max_length=5)
    toughness = models.CharField('Toughness', default='', max_length=5)
    loyalty = models.IntegerField('Loyalty', null=True)
    watermark = models.CharField('Watermark', max_length=20, default='')

    original_text = models.TextField('Original Text')
    original_type = models.TextField('Original Type')


class Rulings(models.Model):
    date = models.DateField('Date')
    text = models.TextField('Text')
    card = models.ForeignKey('Card')


class Set(models.Model):
    SET_TYPE_CORE = 0
    SET_TYPE_EXPANSION = 1
    SET_TYPE_REPRINT = 2
    SET_TYPE_BOX = 3
    SET_TYPE_UN = 4
    SET_TYPE_FROM_THE_VAULT = 5
    SET_TYPE_PREMIUM_DECK = 6
    SET_TYPE_DUEL_DECK = 7
    SET_TYPE_STARTER = 8
    SET_TYPE_COMMANDER = 9
    SET_TYPE_PLANECHASE = 10
    SET_TYPE_ARCHENEMY = 11
    SET_TYPE_PROMO = 12
    SET_TYPE_VANGUARD = 13
    SET_TYPE_MASTERS = 14


    SET_TYPES = (
        (SET_TYPE_CORE, 'Core'),
        (SET_TYPE_EXPANSION, 'Expansion'),
        (SET_TYPE_REPRINT, 'Reprint'),
        (SET_TYPE_BOX, 'Box'),
        (SET_TYPE_UN, 'Un'),
        (SET_TYPE_FROM_THE_VAULT, 'From The Vault'),
        (SET_TYPE_PREMIUM_DECK, 'Premium Deck'),
        (SET_TYPE_DUEL_DECK, 'Duel Deck'),
        (SET_TYPE_STARTER, 'Starter'),
        (SET_TYPE_COMMANDER, 'Commander'),
        (SET_TYPE_PLANECHASE, 'Planechase'),
        (SET_TYPE_ARCHENEMY, 'Archenemy'),
        (SET_TYPE_PROMO, 'Promo'),
        (SET_TYPE_VANGUARD, 'Vanguard'),
        (SET_TYPE_MASTERS, 'Masters')
    )

    @classmethod
    def set_type_from_json(cls, json_str):
        return {human_readable.lower(): db_value for db_value, human_readable in cls.SET_TYPES}.get(json_str, None)

    name = models.CharField('Name', max_length=50)
    code = models.CharField('Code', max_length=4)
    border_color = models.CharField('Border Color', max_length=10)
    release_date = models.DateField('Release Date')
    type = models.IntegerField('Set Type', choices=SET_TYPES)
    block = models.CharField('Block', max_length=20, null=True)
    cards = models.ManyToManyField(Card, through='Printing')


class Format(models.Model):
    sets = models.ManyToManyField(Set)
