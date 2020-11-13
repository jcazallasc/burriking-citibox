import json

from django.core.management.base import BaseCommand

from orders.infrastructure.persistence.django.offer import Offer
from orders.infrastructure.persistence.django.product import Product
from orders.infrastructure.persistence.django.product_option import ProductOption


class Command(BaseCommand):
    """
    Django command to populate the db with products and offers
    """

    PRODUCTS = [
        {
            "id": "e7618a37-6ea8-44f6-ae63-9d999275c3f2",
            "name": "Hamburguesa",
            'base_price': 5.00,
        },
        {
            "id": "9885b9a9-9ce3-4d81-b403-afe12c3671f4",
            "name": "Carne",
            "parent_id": "e7618a37-6ea8-44f6-ae63-9d999275c3f2",
        },
        {
            "id": "30268bd4-62c0-40ca-b7d6-44677fe4e028",
            "name": "Patatas",
            'base_price': 2.00,
        },
        {
            "id": "b28bc2e6-0125-491e-8713-5358924980e8",
            "name": "Refresco",
            'base_price': 1.50,
        },
    ]

    PRODUCT_OPTIONS = [
        {
            "id": "6c64b46a-e784-4b20-ab48-c169b058cd17",
            "product_id": PRODUCTS[0]["id"],
            "label": "Queso",
            "values": json.dumps(["Sin queso", "Con queso cheddar"]),
            "extra_price": 0.00,
        },
        {
            "id": "65db29cb-6dee-499b-b63e-3a8d1e15d386",
            "product_id": PRODUCTS[0]["id"],
            "label": "Tomate",
            "values": json.dumps(["Sin tomate", "Normal", "Cherry"]),
            "extra_price": 0.00,
        },
        {
            "id": "9420a17a-f0db-467b-8fc0-c51d06fb0c2d",
            "product_id": PRODUCTS[1]["id"],
            "label": "Carne",
            "values": json.dumps(["Pollo", "Cerdo", "Pescado"]),
            "extra_price": 0.00,
        },
        {
            "id": "b129657a-b784-4e3f-a208-b7598eb4a6c4",
            "product_id": PRODUCTS[1]["id"],
            "label": "Cocción",
            "values": json.dumps(["Al punto", "Hecha", "Poco hecha"]),
            "extra_price": 0.00,
        },
        {
            "id": "c8822614-e585-4fe9-b39a-9442cf5bb471",
            "product_id": PRODUCTS[1]["id"],
            "label": "Tamaño",
            "values": json.dumps(["125g"]),
            "extra_price": 0.00,
        },
        {
            "id": "c1cea67b-d126-42a3-99f2-c59251c8abcf",
            "product_id": PRODUCTS[1]["id"],
            "label": "Tamaño",
            "values": json.dumps(["250g"]),
            "extra_price": 2.50,
        },
        {
            "id": "7e4b9f61-b806-45fa-98d0-b44b1db8ef1c",
            "product_id": PRODUCTS[1]["id"],
            "label": "Tamaño",
            "values": json.dumps(["350g"]),
            "extra_price": 3.50,
        },
        {
            "id": "9ad18fe3-fe39-4945-89fa-7fdabc0dc889",
            "product_id": PRODUCTS[2]["id"],
            "label": "Tamaño",
            "values": json.dumps(["Pequeño"]),
            "extra_price": 0.0,
        },
        {
            "id": "b5afbf9a-0d26-40c0-bc33-36c2efe709f0",
            "product_id": PRODUCTS[2]["id"],
            "label": "Tamaño",
            "values": json.dumps(["Mediano"]),
            "extra_price": 1.50,
        },
        {
            "id": "d0d23894-7446-49d0-b411-5aff61d1a18a",
            "product_id": PRODUCTS[2]["id"],
            "label": "Tamaño",
            "values": json.dumps(["Grandes"]),
            "extra_price": 2.50,
        },
        {
            "id": "d7f729a5-4505-4c42-b53e-4bbffd322a4c",
            "product_id": PRODUCTS[2]["id"],
            "label": "Tipo",
            "values": json.dumps(["Deluxe", "Gajo", "De la abuela"]),
            "extra_price": 0.0,
        },
        {
            "id": "ab6d5dd0-9f1f-49f5-9d45-edc5ea68caea",
            "product_id": PRODUCTS[3]["id"],
            "label": "Tamaño",
            "values": json.dumps(["Pequeño"]),
            "extra_price": 1.50,
        },
        {
            "id": "5f1dff9b-da53-45e2-a972-37218a1c5c43",
            "product_id": PRODUCTS[3]["id"],
            "label": "Tamaño",
            "values": json.dumps(["Mediano"]),
            "extra_price": 2.50,
        },
        {
            "id": "c06219a6-772c-44ca-bc12-bd07638c2915",
            "product_id": PRODUCTS[3]["id"],
            "label": "Tamaño",
            "values": json.dumps(["Grande"]),
            "extra_price": 3.50,
        },
        {
            "id": "c51a06bd-dec0-4c81-821e-87a6ff12b11e",
            "product_id": PRODUCTS[3]["id"],
            "label": "Tipo",
            "values": json.dumps(["Burricola", "Burribeer", "Brawndo"]),
            "extra_price": 0.0,
        },
    ]

    OFFERS = [
        {
            "id": "563ed1e3-92df-4aef-a38f-d6c50bb5bd30",
            "name": "Euromanía",
            "conditions": json.dumps({
                "days_of_week": [2, 6],
            }),
            "discount": 10,
        },
        {
            "id": "154dea41-086f-4e2a-b73b-632e20170220",
            "name": "Refrescomanía",
            "conditions": json.dumps({
                "days_of_week": [0, 1, 2, 3, 4],
                "combine": [
                    {
                        "product_option_id": PRODUCT_OPTIONS[11]["id"],
                        "quantity": 2,
                    },
                    {
                        "product_id": PRODUCTS[1]["id"],
                        "quantity": 1,
                    },
                ],
            }),
            "discount": 21,
        },
        {
            "id": "3369411f-cc7e-45b5-abc1-cd2210f33eb2",
            "name": "Burrimenu",
            "conditions": json.dumps({
                "days_of_week": [5, 6],
                "combine": [
                    {
                        "product_id": PRODUCTS[0]["id"],
                        "quantity": 1,
                    },
                    {
                        "product_id": PRODUCTS[2]["id"],
                        "quantity": 1,
                    },
                    {
                        "product_id": PRODUCTS[3]["id"],
                        "quantity": 1,
                    },
                ],
            }),
            "discount": 15,
        }
    ]

    def handle(self, *args, **options):
        """
        This is an example of how db can be populated to cover all our scenarios
        """

        self.stdout.write('Populating db...')

        for product in self.PRODUCTS:
            Product.objects.get_or_create(**product)

        for product_option in self.PRODUCT_OPTIONS:
            ProductOption.objects.get_or_create(**product_option)

        for offer in self.OFFERS:
            Offer.objects.get_or_create(**offer)

        self.stdout.write('Finished!!')
