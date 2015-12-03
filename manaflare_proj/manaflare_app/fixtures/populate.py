from io import BytesIO
import requests
import zipfile
import json
from manaflare_app.models import Set


def parse_set(db_alias, set_json):
    Set.objects.using(db_alias).create(name=set_json['name'],
                                       code=set_json['code'],
                                       border_color=set_json['border'],
                                       release_date=set_json['releaseDate'],
                                       type=Set.set_type_from_json(set_json['type']),
                                       block=set_json.get('block', None))


def populate_from_json(db_alias, set_code=None):
    if set_code is not None:
        url = 'http://mtgjson.com/json/{}-x.json.zip'.format(set_code)
    else:
        url = 'http://mtgjson.com/json/AllSetFiles-x.zip'

    response = requests.get(url)
    io = BytesIO()
    io.write(response.content)

    zip = zipfile.ZipFile(io)

    for name in zip.namelist():
        print('Parsing Set {}'.format(name))
        parse_set(db_alias, json.loads(zip.read(name).decode('UTF-8')))


if __name__ == '__main__':
    populate_from_json('2ED')