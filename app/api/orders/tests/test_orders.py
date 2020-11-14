import uuid

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


ORDERS = 'api:api_orders:v1_orders'
ORDER = 'api:api_orders:v1_order'


class OrdersTests(TestCase):
    """ E2E tests working with Orders API """

    def setUp(self):
        self.client = APIClient()

    def test_get_orders(self):
        """Test getting all orders"""

        self.client.post(reverse(
            ORDER,
            kwargs={
                'order_uuid': str(uuid.uuid4()),
            },
        ))

        response = self.client.get(reverse(ORDERS))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.json()))
