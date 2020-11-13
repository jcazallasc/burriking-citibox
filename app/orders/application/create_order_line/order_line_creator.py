from typing import List

from orders.domain.order_repository import OrderRepository
from orders.domain.value_objects.order_line_uuid import OrderLineUUId
from orders.domain.value_objects.order_uuid import OrderUUId
from orders.domain.value_objects.product_option_uuid import ProductOptionUUID
from orders.domain.value_objects.product_uuid import ProductUUID


class OrderLineCreator:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def _validate_options(self, options: List[dict]):
        return [
            {
                "product_option_id": ProductOptionUUID(option["product_option_id"]).value,
                "value": option["value"],
            }
            for option in options
        ]

    def _validate_subproducts(self, subproducts: List[dict]):
        return [
            {
                "subproduct_id": ProductUUID(subproduct["subproduct_id"]).value,
                "subproduct_options": [
                    {
                        "product_option_id": ProductOptionUUID(subproduct_option["product_option_id"]).value,
                        "value": subproduct_option["value"],
                    }
                    for subproduct_option in subproduct["subproduct_options"]

                ]
            }
            for subproduct in subproducts
        ]

    def create(
        self,
        order_uuid: str,
        order_line_uuid: str,
        product_uuid: str,
        options: List[dict],
        subproducts: List[dict],
    ) -> None:
        _order_uuid = OrderUUId(order_uuid)
        _order_line_uuid = OrderLineUUId(order_line_uuid)
        _product_uuid = ProductUUID(product_uuid)
        _options = self._validate_options(options)
        _subproducts = self._validate_subproducts(subproducts)

        self.repository.create_order_line(
            _order_uuid.value,
            _order_line_uuid.value,
            _product_uuid.value,
            _options,
            _subproducts,
        )
