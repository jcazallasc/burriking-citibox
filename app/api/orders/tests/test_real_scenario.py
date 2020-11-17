import json
import uuid

from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from orders.infrastructure.persistence.django.order import Order
from orders.infrastructure.persistence.django.product import Product


ORDER_LINE = 'api:api_orders:v1_order_line'


class OrderLineTests(TestCase):
    """
    E2E tests using API

    Creating a real order. Adding mutiple products with different options.
    """

    def setUp(self):
        self.client = APIClient()
        call_command("populate_db")

        self.order_uuid = str(uuid.uuid4())

        Order.objects.create(id=self.order_uuid)

    def __get_url(self) -> str:
        return reverse(
            ORDER_LINE,
            kwargs={
                'order_uuid': self.order_uuid,
                'order_line_uuid': str(uuid.uuid4()),
            },
        )

    def test_full_order_with_full_menu(self):
        """Test creating a full with a full menu"""

        _hamburguesa = Product.objects.filter(name="Hamburguesa").first()
        _tomate = _hamburguesa.product_options.filter(label="Tomate").first()
        _tomate_value = json.loads(_tomate.values)[0]
        _queso = _hamburguesa.product_options.filter(label="Queso").first()
        _queso_value = json.loads(_queso.values)[0]

        _carne = _hamburguesa.subproducts.filter(name="Carne").first()
        _carne_tamano = _carne.product_options.filter(label="Tamaño").first()
        _carne_tamano_value = json.loads(_carne_tamano.values)[0]
        _carne_coccion = _carne.product_options.filter(label="Cocción").first()
        _carne_coccion_value = json.loads(_carne_coccion.values)[0]
        _carne_tipo = _carne.product_options.filter(label="Carne").first()
        _carne_tipo_value = json.loads(_carne_tipo.values)[0]

        _patata = Product.objects.filter(name="Patatas").first()
        _patata_tipo = _patata.product_options.filter(label="Tipo").first()
        _patata_tipo_value = json.loads(_patata_tipo.values)[0]
        _patata_tamano = _patata.product_options.filter(label="Tamaño").last()
        _patata_tamano_value = json.loads(_patata_tamano.values)[0]

        _refresco = Product.objects.filter(name="Refresco").first()
        _refresco_tipo = _refresco.product_options.filter(label="Tipo").first()
        _refresco_tipo_value = json.loads(_refresco_tipo.values)[0]
        _refresco_tamano = _refresco.product_options.filter(label="Tamaño").last()
        _refresco_tamano_value = json.loads(_refresco_tamano.values)[0]

        subtotal = _hamburguesa.base_price + _carne_tamano.extra_price
        subtotal += _patata.base_price + _patata_tamano.extra_price
        subtotal += _refresco.base_price + _refresco_tamano.extra_price

        self.client.post(self.__get_url(), format='json', data={
            "product_id": str(_patata.id),
            "product_options": [
                {
                    "product_option_id": str(_patata_tipo.id),
                    "value": _patata_tipo_value
                },
                {
                    "product_option_id": str(_patata_tamano.id),
                    "value": _patata_tamano_value
                },
            ],
        })

        self.client.post(self.__get_url(), format='json', data={
            "product_id": str(_refresco.id),
            "product_options": [
                {
                    "product_option_id": str(_refresco_tipo.id),
                    "value": _refresco_tipo_value
                },
                {
                    "product_option_id": str(_refresco_tamano.id),
                    "value": _refresco_tamano_value
                },
            ],
        })

        self.client.post(self.__get_url(), format='json', data={
            "product_id": str(_hamburguesa.id),
            "product_options": [
                {
                    "product_option_id": str(_tomate.id),
                    "value": _tomate_value
                },
                {
                    "product_option_id": str(_queso.id),
                    "value": _queso_value
                },
            ],
            "subproducts": [
                {
                    "subproduct_id": str(_carne.id),
                    "subproduct_options": [
                        {
                            "product_option_id": str(_carne_tamano.id),
                            "value": _carne_tamano_value,
                        },
                        {
                            "product_option_id": str(_carne_coccion.id),
                            "value": _carne_coccion_value,
                        },
                        {
                            "product_option_id": str(_carne_tipo.id),
                            "value": _carne_tipo_value,
                        },
                    ],
                }
            ],
        })

        expected_subtotal = 0
        for line in Order.objects.get(id=self.order_uuid).order_lines.all():
            expected_subtotal += line.subtotal

        self.assertEqual(3, Order.objects.get(id=self.order_uuid).order_lines.count())
        self.assertEqual(subtotal, expected_subtotal)
