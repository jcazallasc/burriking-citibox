from dataclasses import dataclass

from orders.domain.entities.order_line import OrderLine


@dataclass
class Order:
    id: str
    lines: list[OrderLine] = []
