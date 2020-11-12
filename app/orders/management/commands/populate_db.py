import uuid

from django.core.management.base import BaseCommand

from orders.infrastructure.persistence.django.option import Option
from orders.infrastructure.persistence.django.product import Product
from orders.infrastructure.persistence.django.product_option import ProductOption


class Command(BaseCommand):
    """
    Django command to populate the db with products and offers
    """

    PRODUCTS = [
        {
            "id": uuid.uuid4(),
            "name": "Hamburguesa",
            'base_price': 5.00,
        },
        {
            "id": uuid.uuid4(),
            "name": "Patatas",
            'base_price': 2.00,
        },
        {
            "id": uuid.uuid4(),
            "name": "Refresco",
            'base_price': 1.50,
        },
    ]

    OPTIONS = [
        {
            "id": uuid.uuid4(),
            "label": "125g",
            "group": "Hamburguesa size",
            "extra_price": 0.00,
        },
        {
            "id": uuid.uuid4(),
            "label": "250g",
            "group": "Hamburguesa size",
            "extra_price": 2.50,
        },
        {
            "id": uuid.uuid4(),
            "label": "350g",
            "group": "Hamburguesa size",
            "extra_price": 3.50,
        },
        {
            "id": uuid.uuid4(),
            "label": "Pollo",
            "group": "Hamburguesa type",
            "extra_price": 0.0,
        },
        {
            "id": uuid.uuid4(),
            "label": "Cerdo",
            "group": "Hamburguesa type",
            "extra_price": 0.0,
        },
        {
            "id": uuid.uuid4(),
            "label": "Pequeña",
            "group": "Patatas size",
            "extra_price": 2.00,
        },
        {
            "id": uuid.uuid4(),
            "label": "Mediano",
            "group": "Patatas size",
            "extra_price": 1.50,
        },
        {
            "id": uuid.uuid4(),
            "label": "Grandes",
            "group": "Patatas size",
            "extra_price": 2.50,
        },
        {
            "id": uuid.uuid4(),
            "label": "Pequeño",
            "group": "Refresco size",
            "extra_price": 1.50,
        },
        {
            "id": uuid.uuid4(),
            "label": "Mediano",
            "group": "Refresco size",
            "extra_price": 2.50,
        },
        {
            "id": uuid.uuid4(),
            "label": "Grande",
            "group": "Refresco size",
            "extra_price": 3.50,
        },
    ]

    PRODUCT_OPTIONS = [
        {
            "id": uuid.uuid4(),
            "product_id": PRODUCTS[0]["id"],
            "option_id": OPTIONS[0]["id"],
        },
        {
            "id": uuid.uuid4(),
            "product_id": PRODUCTS[0]["id"],
            "option_id": OPTIONS[1]["id"],
        },
        {
            "id": uuid.uuid4(),
            "product_id": PRODUCTS[0]["id"],
            "option_id": OPTIONS[2]["id"],
        },
        {
            "id": uuid.uuid4(),
            "product_id": PRODUCTS[0]["id"],
            "option_id": OPTIONS[3]["id"],
        },
        {
            "id": uuid.uuid4(),
            "product_id": PRODUCTS[0]["id"],
            "option_id": OPTIONS[4]["id"],
        }
    ]

    OFFERS = [
        {
            "id": uuid.uuid4(),
            "name": "Euromanía",
            "conditions": {
                "day_of_week": [2, 6],
            },
            "discount": 10,
        },
        {
            "id": uuid.uuid4(),
            "name": "Refrescomanía",
            "conditions": {
                "day_of_week": [0, 1, 2, 3, 4],
                "combine": [
                    {
                        "product_option_id": OPTIONS[0]["id"],
                        "quantity": 2,
                    },
                ],
            },
            "discount": 21,
        },
        {
            "id": uuid.uuid4(),
            "name": "Burrimenu",
            "conditions": {
                "day_of_week": [5, 6],
                "combine": [
                    {
                        "product_id": PRODUCTS[0]["id"],
                        "quantity": 1,
                    },
                    {
                        "product_id": PRODUCTS[1]["id"],
                        "quantity": 1,
                    },
                    {
                        "product_id": PRODUCTS[2]["id"],
                        "quantity": 1,
                    },
                ],
            },
            "discount": 21,
        }
    ]

    def handle(self, *args, **options):
        """
        This is an example of how db can be populated to cover all our scenarios
        """

        if Option.objects.all().count() and Product.objects.all().count():
            return

        for option in self.OPTIONS:
            Option.objects.create(**option)

        for product in self.PRODUCTS:
            Product.objects.create(**product)

        for product_option in self.PRODUCT_OPTIONS:
            ProductOption.objects.create(**product_option)
