import uuid

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from orders.domain.exceptions.invalid_uuid import InvalidUUID
from orders.domain.exceptions.order_does_not_exist import OrderDoesNotExist
from orders.infrastructure.persistence.django.order import Order


ORDER = 'api:api_orders:v1_order'


class OrderTests(TestCase):
    """
    E2E tests using Order API 

    Creating order
    Deleting order

    """

    def setUp(self):
        self.client = APIClient()

    def test_create_order(self):
        """Test creating order"""

        order_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER,
            kwargs={
                'order_uuid': order_uuid,
            },
        )

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, Order.objects.filter(id=order_uuid).count())

    def test_create_order_with_invalid_uuid(self):
        """Test creating order with invalid uuid"""

        order_uuid = "error"

        url = reverse(
            ORDER,
            kwargs={
                'order_uuid': order_uuid,
            },
        )

        with self.assertRaises(InvalidUUID):
            self.client.post(url)

    def test_remove_order(self):
        """Test remove existing order"""

        order_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER,
            kwargs={
                'order_uuid': order_uuid,
            },
        )

        self.client.post(url)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, Order.objects.filter(id=order_uuid).count())

    def test_remove_non_existing_order(self):
        """Test remove non existing order"""

        order_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER,
            kwargs={
                'order_uuid': order_uuid,
            },
        )

        with self.assertRaises(OrderDoesNotExist):
            self.client.delete(url)
