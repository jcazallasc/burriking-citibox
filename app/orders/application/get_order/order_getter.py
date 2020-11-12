from orders.domain.entities.order_entity import OrderEntity
from orders.domain.order_repository import OrderRepository
from orders.domain.value_objects.order_uuid import OrderUUId


class OrderGetter:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def get_order_data(self, order_uuid: str) -> dict:
        _order_uuid = OrderUUId(order_uuid)

        return self.to_response(self.repository.get_order_data(_order_uuid.value))

    def to_response(self, order: OrderEntity) -> dict:
        return order.to_dict()
