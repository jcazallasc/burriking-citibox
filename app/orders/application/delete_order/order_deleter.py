from orders.domain.order_repository import OrderRepository
from orders.domain.value_objects.order_id import OrderId


class OrderDeleter:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create(self, order_id: int) -> None:
        _order_id = OrderId(order_id)

        self.repository.delete(_order_id.value)
