from orders.domain.order_repository import OrderRepository
from orders.domain.value_objects.order_uuid import OrderUUId


class OrderCreator:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create(self, order_uuid: str) -> None:
        _order_uuid = OrderUUId(order_uuid)

        self.repository.create(_order_uuid.value)
