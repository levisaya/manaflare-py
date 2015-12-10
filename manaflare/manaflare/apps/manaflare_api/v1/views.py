from rest_framework import viewsets
from manaflare.apps.manaflare_api.v1.models import Card, SuperType, Type, SubType, Set, Printing
from manaflare.apps.manaflare_api.v1 import serializers
from rest_framework.generics import ListAPIView


class SuperTypeViewSet(viewsets.ModelViewSet):
    queryset = SuperType.objects.order_by('value').all()
    serializer_class = serializers.SuperTypeSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.order_by('value').all()
    serializer_class = serializers.TypeSerializer


class SubTypeViewSet(viewsets.ModelViewSet):
    queryset = SubType.objects.order_by('value').all()
    serializer_class = serializers.SubTypeSerializer


class CardViewSet(viewsets.ModelViewSet):
    lookup_field = 'name'
    queryset = Card.objects.all()
    serializer_class = serializers.CardSerializer


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = serializers.SetSerializer


class PrintingViewSet(viewsets.ModelViewSet):
    lookup_field = 'hash_id'
    queryset = Printing.objects.all()
    serializer_class = serializers.PrintingSerializer