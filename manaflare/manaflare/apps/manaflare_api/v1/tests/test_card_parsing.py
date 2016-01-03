from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CardTests(APITestCase):
    fixtures = ['manaflare/apps/manaflare_api/v1/tests/fixtures/ISD+BFZ.json']

    def test_card_parse(self):
        url = reverse('card-detail', args=("Altar's Reap",))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        from pprint import pprint

        pprint(response.data)