from rest_framework import serializers
from manaflare.apps.manaflare_api.models import Card, CardType, CardColors, Set, Printing, TypeLinkage
from rest_framework.reverse import reverse


class ColorField(serializers.RelatedField):
    def to_representation(self, obj):
        return CardColors.COLORS[obj.color]


class TypeField(serializers.RelatedField):
    def to_representation(self, obj):
        pass


class CardColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardColors
        fields = ('color',)


class PrintingListingField(serializers.RelatedField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'hash_id': obj.hash_id
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def to_representation(self, value):
        duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return 'Track %d: %s (%s)' % (value.order, value.name, duration)


class TypeLinkageSerializer(serializers.ModelSerializer):
    type = serializers.ReadOnlyField(source='type.value')

    class Meta:
        model = TypeLinkage
        fields = ('type', 'supertype', 'subtype')


class CardSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='card-detail', lookup_field='name')
    colors = ColorField(many=True, read_only=True)
    color_identity = ColorField(many=True, read_only=True)
    types = TypeLinkageSerializer(source='typelinkage_set', many=True)
    printings = PrintingListingField

    class Meta:
        model = Card
        lookup_field = 'name'


class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set


class PrintingSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='printing-detail', lookup_field='hash_id')
    artist = serializers.SlugRelatedField(read_only=True, slug_field='name')
    card = CardSerializer()

    class Meta:
        model = Printing
        lookup_field = 'hash_id'
