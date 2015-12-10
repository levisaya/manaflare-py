from rest_framework import serializers
from manaflare.apps.manaflare_api.v1.models import Card, SuperType, Type, SubType, CardColors, Set, Printing
from rest_framework.reverse import reverse


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


# class PrintingListingField(serializers.RelatedField):
#     def get_url(self, obj, view_name, request, format):
#         url_kwargs = {
#             'name': obj.organization.slug,
#         }
#         return reverse(view_name, kwargs=url_kwargs, request=request, format=format)
#
#     def to_representation(self, value):
#         duration = time.strftime('%M:%S', time.gmtime(value.duration))
#         return 'Track %d: %s (%s)' % (value.order, value.name, duration)


class CardSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='card-detail', lookup_field='name')
    colors = CardColorSerializer(many=True)
    color_identity = CardColorSerializer(many=True)
    # printings = PrintingListingField

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
