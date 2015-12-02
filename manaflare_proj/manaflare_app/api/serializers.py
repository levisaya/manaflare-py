from rest_framework import serializers
from manaflare_app.models import Card, SuperType, Type, SubType, CardColors


class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ('value',)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('value',)


class SubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubType
        fields = ('value',)


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card


class CardColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardColors
        fields = ('color',)