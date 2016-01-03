from rest_framework import viewsets
from manaflare.apps.manaflare_api.models import Card, CardType, Set, Printing
from manaflare.apps.manaflare_api.v1 import serializers
from rest_framework.generics import ListAPIView


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