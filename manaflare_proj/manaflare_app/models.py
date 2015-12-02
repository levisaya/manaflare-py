from django.db import models
from enum import Enum


# class EnumField(models.IntegerField):
#     __metaclass__ = models.SubfieldBase
#
#     def __init__(self, **kwargs):
#         self.choice_enum = kwargs['choices']
#         kwargs['choices'] = ((choice.value, choice.name) for choice in kwargs['choices'])
#         super(models.IntegerField, self).__init__(**kwargs)
#
#     def to_python(self, value):
#         return self.choice_enum(value).name
#
#     def get_db_prep_value(self, choice):
#         return self.choice_enum[choice]


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
    color = models.CharField('Color', max_length=10)

    def __str__(self):
        return self.color


class CardLayouts(Enum):
    Normal = 0
    Split = 1
    Flip = 2
    DoubleFaced = 3
    Token = 4
    Plane = 5
    Scheme = 6
    Phenomenon = 7
    Leveler = 8
    Vanguard = 9

    # labels = {Normal: 'Normal',
    #           Split: 'Split',
    #           Flip: 'Flip',
    #           DoubleFaced: 'DoubleFaced',
    #           Token: 'Token',
    #           Plane: 'Plane',
    #           Scheme: 'Scheme',
    #           Phenomenon: 'Phenomenon',
    #           Leveler: 'Leveler',
    #           Vanguard: 'Vanguard'}


class Rarity(Enum):
    Common = 0
    Uncommon = 1
    Rare = 2
    MythicRare = 3
    Special = 4
    BasicLand = 5


class Printing(models.Model):
    rarity = EnumField(choices=Rarity, default=Rarity.Common)
    flavor = models.TextField('Flavor Text')
    artist = models.ForeignKey('Artist')
    number = models.CharField('Card Number', max_length=5)
    multiverse_id = models.IntegerField('Multiverse Id')
    variations = SeparatedValuesField()
    border = models.CharField('Border Color', max_length=10)
    timeshifted = models.BooleanField('Is Timeshifted')

    card = models.ForeignKey('Card')
    set = models.ForeignKey('Set')


class Card(models.Model):
    hash_id = models.CharField('id', unique=True, max_length=50)
    layout = EnumField(choices=CardLayouts, default=CardLayouts.Normal)
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
    toughness = models.CharField('Power', default='', max_length=5)
    loyalty = models.IntegerField('Loyalty', null=True)
    watermark = models.CharField('Watermark', max_length=20, default='')

    original_text = models.TextField('Original Text')
    original_type = models.TextField('Original Type')


class Rulings(models.Model):
    date = models.DateField('Date')
    text = models.TextField('Text')
    card = models.ForeignKey('Card')


class SetType(Enum):
    Core = 0
    Expansion = 1
    Reprint = 2
    Box = 3
    Un = 4
    FromTheVault = 5
    PremiumDeck = 6
    DuelDeck = 7
    Starter = 8
    Commander = 9
    Planechase = 10
    Archenemy = 11
    Promo = 12
    Vanguard = 13
    Masters = 14

#     labels = {Core: 'Core',
#               Expansion: 'Expansion',
#               Reprint: 'Reprint',
#               Box: 'Box',
#               Un: 'Un',
#               FromTheVault: 'FromTheVault',
#               PremiumDeck: 'PremiumDeck',
#               DuelDeck: 'DuelDeck',
#               Starter: 'Starter',
#               Commander: 'Commander',
#               Planechase: 'Planechase',
#               Archenemy: 'Archenemy',
#               Promo: 'Promo',
#               Vanguard: 'Vanguard',
#               Masters: 'Masters'}


class Set(models.Model):
    name = models.CharField('Name', max_length=50)
    code = models.CharField('Code', max_length=4)
    border_color = models.CharField('Border Color', max_length=10)
    release_date = models.DateField('Release Date')
    type = EnumField(choices=SetType, default=SetType.Expansion)
    block = models.CharField('Block', max_length=20)
    cards = models.ManyToManyField(Card, through='Printing')


class Format(models.Model):
    sets = models.ManyToManyField(Set)
