from rest_framework import viewsets
from manaflare_app.models import Card, SuperType, Type, SubType, CardColors
from manaflare_app.api.serializers import CardSerializer, SuperTypeSerializer, TypeSerializer, SubTypeSerializer, CardColorSerializer


class SuperTypeViewSet(viewsets.ModelViewSet):
    queryset = SuperType.objects.order_by('value').all()
    serializer_class = SuperTypeSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.order_by('value').all()
    serializer_class = TypeSerializer


class SubTypeViewSet(viewsets.ModelViewSet):
    queryset = SubType.objects.order_by('value').all()
    serializer_class = SubTypeSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardColorViewSet(viewsets.ModelViewSet):
    queryset = CardColors.objects.all()
    serializer_class = CardColorSerializer