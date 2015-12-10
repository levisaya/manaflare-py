from io import BytesIO
import requests
import zipfile
import json
from manaflare.apps.manaflare_api.v1.models import Set, Artist, Format, Printing, CardColors, Card, SuperType, Type, SubType, FormatRelationship
from django.core.exceptions import ObjectDoesNotExist


def parse_set(db_alias, set_json):
    colors = {color_str: CardColors.objects.using(db_alias).get(color=color) for color, color_str in CardColors.COLORS}

    color_identities = {
        'W': colors['White'],
        'U': colors['Blue'],
        'R': colors['Red'],
        'G': colors['Green'],
        'B': colors['Black']
    }

    set = Set.objects.using(db_alias).create(name=set_json['name'],
                                             code=set_json['code'],
                                             border_color=set_json['border'],
                                             release_date=set_json['releaseDate'],
                                             type=Set.set_type_from_json(set_json['type']),
                                             block=set_json.get('block', None))

    for card in set_json['cards']:
        artist, _ = Artist.objects.using(db_alias).get_or_create(name=card['artist'])

        supertypes = [SuperType.objects.using(db_alias).get_or_create(value=super_type)[0] for super_type in card.get('supertypes', [])]
        types = [Type.objects.using(db_alias).get_or_create(value=_type)[0] for _type in card.get('types', [])]
        subtypes = [SubType.objects.using(db_alias).get_or_create(value=_type)[0] for _type in card.get('subtypes', [])]

        card_record = None

        try:
            card_record = Card.objects.using(db_alias).get(name=card['name'])
        except ObjectDoesNotExist:
            pass

        if card_record is None:
            card_record = Card.objects.using(db_alias).create(layout=Card.layout_from_json(card['layout']),
                                                              name=card['name'],
                                                              names=card.get('names', []),
                                                              mana_cost=card.get('manaCost', None),
                                                              cmc=card.get('cmc', None),
                                                              type=card['type'],
                                                              text=card.get('text', ''),
                                                              power=card.get('power', None),
                                                              toughness=card.get('toughness', None),
                                                              loyalty=card.get('loyalty', None),
                                                              watermark=card.get('watermark', None),
                                                              original_text=card.get('original_text', None),
                                                              original_type=card.get('original_type', None))

            for color_str in card.get('colors', []):
                card_record.colors.add(colors[color_str])

            for color_str in card.get('colorIdentity', []):
                card_record.color_identity.add(color_identities[color_str])

            card_record.supertypes = supertypes
            card_record.types = types
            card_record.subtypes = subtypes
            card_record.save()

        printing = Printing.objects.using(db_alias).create(hash_id=card['id'],
                                                           rarity=Printing.rarity_from_json(card['rarity']),
                                                           flavor=card.get('flavor', None),
                                                           artist=artist,
                                                           number=card.get('number', None),
                                                           multiverse_id=card.get('multiverseid', None),
                                                           variations=card.get('variations', []),
                                                           border=card.get('border', None),
                                                           timeshifted=card.get('timeshifted', False),
                                                           card=card_record,
                                                           set=set)

        for legality in card.get('legalities', []):
            format, _ = Format.objects.using(db_alias).get_or_create(name=legality['format'])

            FormatRelationship.objects.using(db_alias).create(card=card_record,
                                                              format=format,
                                                              status=FormatRelationship.legality_from_json(legality['legality']))


def populate_from_json(db_alias, set_codes=None):
    urls = []
    if set_codes is not None:
        for set_code in set_codes:
            urls.append('http://mtgjson.com/json/{}-x.json.zip'.format(set_code))
    else:
        urls.append('http://mtgjson.com/json/AllSetFiles-x.zip')

    for url in urls:
        response = requests.get(url)
        io = BytesIO()
        io.write(response.content)

        zip = zipfile.ZipFile(io)

        for name in zip.namelist():
            parse_set(db_alias, json.loads(zip.read(name).decode('UTF-8')))


if __name__ == '__main__':
    populate_from_json('2ED')