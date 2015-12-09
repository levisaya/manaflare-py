from rest_framework import serializers
from manaflare.apps.manaflare_api.v1.models import Card, SuperType, Type, SubType, CardColors, Set


class SuperTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuperType
        fields = ('value',)


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('value',)


class SubTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubType
        fields = ('value',)


class CardColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardColors
        fields = ('color',)


class CardSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='card-detail', lookup_field='name')
    colors = CardColorSerializer(many=True)
    color_identity = CardColorSerializer(many=True)


    class Meta:
        model = Card
        lookup_field = 'name'


class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set