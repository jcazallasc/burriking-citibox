from orders.domain.order_repository import OrderRepository
from orders.domain.value_objects.order_uuid import OrderUUId


class OrderDeleter:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def delete(self, order_uuid: str) -> None:
        _order_uuid = OrderUUId(order_uuid)

        self.repository.delete(_order_uuid.value)
