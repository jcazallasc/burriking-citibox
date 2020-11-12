from typing import List

from orders.domain.entities.order_entity import OrderEntity
from orders.domain.order_repository import OrderRepository
from orders.domain.value_objects.order_uuid import OrderUUId


class OrderList:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def list(self) -> List[dict]:
        return self.to_response(self.repository.get_orders_data())

    def to_response(self, orders: List[OrderEntity]) -> List[dict]:
        _response = []

        for _order in orders:
            _response.append(_order.to_dict())

        return _response
