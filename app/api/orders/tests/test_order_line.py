import json
import uuid

from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from orders.domain.exceptions.order_line_does_not_exist import OrderLineDoesNotExist
from orders.infrastructure.persistence.django.order import Order
from orders.infrastructure.persistence.django.order_line import OrderLine
from orders.infrastructure.persistence.django.product import Product


ORDER_LINE = 'api:api_orders:v1_order_line'


class OrderLineTests(TestCase):
    """ E2E tests working with OrderLine API """

    def setUp(self):
        self.client = APIClient()
        call_command("populate_db")

        self.order_uuid = str(uuid.uuid4())

        self.product = Product.objects.first()
        self.product_option = self.product.product_options.first()

        self.last_product = Product.objects.last()
        self.last_product_option = self.last_product.product_options.first()

        self.subproduct = Product.objects.exclude(parent_id=None).first()
        self.subproduct_option = self.subproduct.product_options.first()
        self.subproduct_parent = self.subproduct.parent
        self.subproduct_parent_option = self.subproduct_parent.product_options.first()

        Order.objects.create(id=self.order_uuid)

    def test_create_order_line(self):
        """Test creating order line"""

        order_line_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER_LINE,
            kwargs={
                'order_uuid': self.order_uuid,
                'order_line_uuid': order_line_uuid,
            },
        )

        subtotal = self.product.base_price + self.product_option.extra_price

        response = self.client.post(url, format='json', data={
            "product_id": str(self.product.id),
            "product_options": [
                {
                    "product_option_id": str(self.product_option.id),
                    "value": str(json.loads(self.product_option.values)[0])
                },
            ],
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, Order.objects.filter(id=self.order_uuid).count())
        self.assertEqual(1, Order.objects.get(id=self.order_uuid).order_lines.count())
        self.assertEqual(subtotal, Order.objects.get(id=self.order_uuid).order_lines.first().subtotal)

    def test_create_order_line_with_invalid_params(self):
        """Test creating order with invalid params"""

        order_line_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER_LINE,
            kwargs={
                'order_uuid': self.order_uuid,
                'order_line_uuid': order_line_uuid,
            },
        )

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_remove_order_line(self):
        """Test remove existing order line"""

        order_line_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER_LINE,
            kwargs={
                'order_uuid': self.order_uuid,
                'order_line_uuid': order_line_uuid,
            },
        )

        self.client.post(url, format='json', data={
            "product_id": str(self.product.id),
            "product_options": [
                {
                    "product_option_id": str(self.product_option.id),
                    "value": str(json.loads(self.product_option.values)[0])
                },
            ],
        })
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, Order.objects.get(id=self.order_uuid).order_lines.count())

    def test_remove_non_existing_order_line(self):
        """Test remove non existing order line"""

        order_line_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER_LINE,
            kwargs={
                'order_uuid': self.order_uuid,
                'order_line_uuid': order_line_uuid,
            },
        )

        with self.assertRaises(OrderLineDoesNotExist):
            self.client.delete(url)

    def test_check_total_order(self):
        """Checking total order is right when adding order line"""

        order_line_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER_LINE,
            kwargs={
                'order_uuid': self.order_uuid,
                'order_line_uuid': order_line_uuid,
            },
        )

        subtotal = self.product.base_price + self.product_option.extra_price

        self.client.post(url, format='json', data={
            "product_id": str(self.product.id),
            "product_options": [
                {
                    "product_option_id": str(self.product_option.id),
                    "value": str(json.loads(self.product_option.values)[0])
                },
            ],
        })

        self.assertEqual(subtotal, OrderLine.objects.get(id=order_line_uuid).subtotal)
        self.assertTrue(0.0 != Order.objects.get(id=self.order_uuid).total)

    def test_create_order_line_with_subproducts(self):
        """Test creating order line with subproducts"""

        order_line_uuid = str(uuid.uuid4())

        url = reverse(
            ORDER_LINE,
            kwargs={
                'order_uuid': self.order_uuid,
                'order_line_uuid': order_line_uuid,
            },
        )

        subtotal = self.subproduct_parent.base_price + self.subproduct_parent_option.extra_price
        subtotal += self.subproduct_option.extra_price

        response = self.client.post(url, format='json', data={
            "product_id": str(self.subproduct_parent.id),
            "product_options": [
                {
                    "product_option_id": str(self.subproduct_parent_option.id),
                    "value": str(json.loads(self.subproduct_parent_option.values)[0])
                },
            ],
            "subproducts": [
                {
                    "subproduct_id": str(self.subproduct.id),
                    "subproduct_options": [
                        {
                            "product_option_id": str(self.subproduct_option.id),
                            "value": str(json.loads(self.subproduct_option.values)[0])
                        },
                    ],
                }
            ],
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, Order.objects.filter(id=self.order_uuid).count())
        self.assertEqual(1, Order.objects.get(id=self.order_uuid).order_lines.count())
        self.assertEqual(subtotal, Order.objects.get(id=self.order_uuid).order_lines.first().subtotal)
