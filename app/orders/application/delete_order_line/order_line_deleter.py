from orders.domain.order_repository import OrderRepository
from orders.domain.value_objects.order_line_uuid import OrderLineUUId


class OrderLineDeleter:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def delete(self, order_line_uuid: str) -> None:
        _order_line_uuid = OrderLineUUId(order_line_uuid)

        self.repository.delete_order_line(_order_line_uuid.value)
