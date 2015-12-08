from rest_framework import viewsets
from manaflare.apps.manaflare_api.v1.models import Card, SuperType, Type, SubType, Set
from manaflare.apps.manaflare_api.v1.serializers import CardSerializer, SuperTypeSerializer, TypeSerializer, SubTypeSerializer, SetSerializer


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
    # lookup_field = 'name'
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer