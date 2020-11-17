from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from orders.domain.entities.offer_entity import OfferEntity
from orders.domain.entities.order_entity import OrderEntity
from orders.domain.entities.order_line_entity import OrderLineEntity
from orders.domain.entities.product_option_entity import ProductOptionEntity
from orders.domain.entities.subproduct_entity import SubproductEntity
from orders.domain.offers.days_of_week_checker import DaysOfWeekChecker


ORDER_LINE = 'api:api_orders:v1_order_line'


class OfferTests(TestCase):
    """
    Tests to checking the offer logic

    Checking when daily offer applies

    Checking when daily offer applies + Having a specific product in the order

    Checking when daily offer applies + Having a specific product in the order

    Checking when daily offer applies + Having a specific product in the order and/or product option

    Checking when daily offer applies + Having a specific subproduct in the order and/or subproduct option
    """

    def setUp(self):
        self.client = APIClient()

    @patch.object(DaysOfWeekChecker, "_current_day_of_week", return_value=1)
    def test_daily_offer(self, mock_current_day_of_week):
        """
        Test happy path. Offer should be applied.
        """

        offer = OfferEntity(
            id="OfferTest",
            name="OfferTest",
            conditions={
                "days_of_week": [1, 2],
            },
            discount=10,
        )

        order = OrderEntity(
            id="OrderTest",
            lines=[
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=5.0,
                    product_options=[],
                    subproducts=[],
                    subtotal=10.0,
                )

            ],
            total=0.0,
            offer_id="",
            offer_name="",
        )

        self.assertEqual(0.0, order.total)

        order.calculate_total([offer])

        self.assertTrue(mock_current_day_of_week.called)
        self.assertEqual(9.0, order.total)
        self.assertEqual(offer.id, order.offer_id)
        self.assertEqual(offer.name, order.offer_name)

    @patch.object(DaysOfWeekChecker, "_current_day_of_week", return_value=1)
    def test_daily_offer_not_apply(self, mock_current_day_of_week):
        """
        Test daily offer doesn't apply because of the day doesn't match
        """

        offer = OfferEntity(
            id="OfferTest",
            name="OfferTest",
            conditions={
                "days_of_week": [2, 5],
            },
            discount=10,
        )

        order = OrderEntity(
            id="OrderTest",
            lines=[
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=5.0,
                    product_options=[],
                    subproducts=[],
                    subtotal=10.0,
                )

            ],
            total=0.0,
            offer_id="",
            offer_name="",
        )

        self.assertEqual(0.0, order.total)

        order.calculate_total([offer])

        self.assertTrue(mock_current_day_of_week.called)
        self.assertEqual(10.0, order.total)

    @patch.object(DaysOfWeekChecker, "_current_day_of_week", return_value=1)
    def test_apply_lowest_offer(self, mock_current_day_of_week):
        """
        Test getting the lowest offer when multiple offers apply
        """

        offer1 = OfferEntity(
            id="OfferTest1",
            name="OfferTest1",
            conditions={
                "days_of_week": [1, 2, 5],
            },
            discount=5,
        )

        offer2 = OfferEntity(
            id="OfferTest2",
            name="OfferTest2",
            conditions={
                "days_of_week": [1, 6],
            },
            discount=20,
        )

        order = OrderEntity(
            id="OrderTest",
            lines=[
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=5.0,
                    product_options=[],
                    subproducts=[],
                    subtotal=10.0,
                )

            ],
            total=0.0,
            offer_id="",
            offer_name="",
        )

        self.assertEqual(0.0, order.total)

        order.calculate_total([offer1, offer2])

        self.assertTrue(mock_current_day_of_week.called)
        self.assertEqual(9.50, order.total)

    @patch.object(DaysOfWeekChecker, "_current_day_of_week", return_value=1)
    def test_offer_with_product_id(self, mock_current_day_of_week):
        """
        Testing if the offer applies when check days_of_week and product_id
        """

        offer1 = OfferEntity(
            id="OfferTest1",
            name="OfferTest1",
            conditions={
                "days_of_week": [1, 2, 5],
                "combine": [
                    {
                        "product_id": "1",
                        "quantity": 1,
                    }
                ],
            },
            discount=10,
        )

        order = OrderEntity(
            id="OrderTest",
            lines=[
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=10.0,
                    product_options=[],
                    subproducts=[],
                    subtotal=10.0,
                )

            ],
            total=0.0,
            offer_id="",
            offer_name="",
        )

        self.assertEqual(0.0, order.total)

        order.calculate_total([offer1])

        self.assertTrue(mock_current_day_of_week.called)
        self.assertEqual(9.00, order.total)

    @patch.object(DaysOfWeekChecker, "_current_day_of_week", return_value=1)
    def test_offer_with_more_than_1_product_id(self, mock_current_day_of_week):
        """
        Testing if the offer applies when match product_id and quantity
        """

        offer1 = OfferEntity(
            id="OfferTest1",
            name="OfferTest1",
            conditions={
                "days_of_week": [1, 2, 5],
                "combine": [
                    {
                        "product_id": "1",
                        "quantity": 2,
                    }
                ],
            },
            discount=10,
        )

        order = OrderEntity(
            id="OrderTest",
            lines=[
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=10.0,
                    product_options=[],
                    subproducts=[],
                    subtotal=10.0,
                ),
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=10.0,
                    product_options=[],
                    subproducts=[],
                    subtotal=10.0,
                )
            ],
            total=0.0,
            offer_id="",
            offer_name="",
        )

        self.assertEqual(0.0, order.total)

        order.calculate_total([offer1])

        self.assertTrue(mock_current_day_of_week.called)
        self.assertEqual(18.00, order.total)

    @patch.object(DaysOfWeekChecker, "_current_day_of_week", return_value=1)
    def test_offer_with_more_than_1_product_id_failing(self, mock_current_day_of_week):
        """
        Testing if the offer is not applied when quantity mismatch
        """

        offer1 = OfferEntity(
            id="OfferTest1",
            name="OfferTest1",
            conditions={
                "days_of_week": [1, 2, 5],
                "combine": [
                    {
                        "product_id": "1",
                        "quantity": 3,
                    }
                ],
            },
            discount=10,
        )

        order = OrderEntity(
            id="OrderTest",
            lines=[
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=10.0,
                    product_options=[],
                    subproducts=[],
                    subtotal=10.0,
                ),
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=10.0,
                    product_options=[],
                    subproducts=[],
                    subtotal=10.0,
                )
            ],
            total=0.0,
            offer_id="",
            offer_name="",
        )

        self.assertEqual(0.0, order.total)

        order.calculate_total([offer1])

        self.assertTrue(mock_current_day_of_week.called)
        self.assertEqual(20.00, order.total)

    @patch.object(DaysOfWeekChecker, "_current_day_of_week", return_value=1)
    def test_offer_with_product_id_and_option(self, mock_current_day_of_week):
        """
        Testing if the offer works correctly checking in product_id and product_options
        """

        offer1 = OfferEntity(
            id="OfferTest1",
            name="OfferTest1",
            conditions={
                "days_of_week": [1, 2, 5],
                "combine": [
                    {
                        "product_id": "1",
                        "quantity": 1,
                    },
                    {
                        "product_option_id": "2",
                        "quantity": 2,
                    }
                ],
            },
            discount=10,
        )

        order = OrderEntity(
            id="OrderTest",
            lines=[
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=5.0,
                    product_options=[
                        ProductOptionEntity(
                            id="2",
                            label="OptionTest",
                            values=[],
                            extra_price=5.00,
                        ),
                        ProductOptionEntity(
                            id="2",
                            label="OptionTest",
                            values=[],
                            extra_price=5.00,
                        )
                    ],
                    subproducts=[],
                    subtotal=15.0,
                )
            ],
            total=0.0,
            offer_id="",
            offer_name="",
        )

        self.assertEqual(0.0, order.total)

        order.calculate_total([offer1])

        self.assertTrue(mock_current_day_of_week.called)
        self.assertEqual(13.50, order.total)

    @patch.object(DaysOfWeekChecker, "_current_day_of_week", return_value=1)
    def test_offer_with_product_id_and_subproduct(self, mock_current_day_of_week):
        """
        Testing if the offer works correctly checking in product_options and subproducts
        """

        offer1 = OfferEntity(
            id="OfferTest1",
            name="OfferTest1",
            conditions={
                "days_of_week": [1, 2, 5],
                "combine": [
                    {
                        "product_id": "1",
                        "quantity": 1,
                    },
                    {
                        "product_option_id": "2",
                        "quantity": 2,
                    }
                ],
            },
            discount=10,
        )

        order = OrderEntity(
            id="OrderTest",
            lines=[
                OrderLineEntity(
                    id="OrderLineTest",
                    product_id="1",
                    product_name="OrderLineTest",
                    product_base_price=5.0,
                    product_options=[
                        ProductOptionEntity(
                            id="2",
                            label="OptionTest",
                            values=[],
                            extra_price=5.00,
                        )
                    ],
                    subproducts=[
                        SubproductEntity(
                            subproduct_name="TestSubproduct",
                            subproduct_options=[
                                {
                                    "id": "2",
                                    "value": "TestValue",
                                    "extra_price": 5.00
                                }
                            ]
                        )
                    ],
                    subtotal=15.0,
                )
            ],
            total=0.0,
            offer_id="",
            offer_name="",
        )

        self.assertEqual(0.0, order.total)

        order.calculate_total([offer1])

        self.assertTrue(mock_current_day_of_week.called)
        self.assertEqual(13.50, order.total)
