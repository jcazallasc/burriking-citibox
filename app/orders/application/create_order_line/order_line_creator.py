from typing import List

from orders.domain.order_repository import OrderRepository
from orders.domain.value_objects.order_line_uuid import OrderLineUUId
from orders.domain.value_objects.order_uuid import OrderUUId
from orders.domain.value_objects.product_option_uuid import ProductOptionUUID
from orders.domain.value_objects.product_uuid import ProductUUID


class OrderLineCreator:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create(self, order_uuid: str, order_line_uuid: str, product_uuid: str, options: List[str]) -> None:
        _order_uuid = OrderUUId(order_uuid)
        _order_line_uuid = OrderLineUUId(order_line_uuid)
        _product_uuid = ProductUUID(product_uuid)
        _options = [ProductOptionUUID(option).value for option in options]

        self.repository.create_order_line(_order_uuid.value, _order_line_uuid.value, _product_uuid.value, _options)
