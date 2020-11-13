from dataclasses import dataclass
from typing import List, Optional

from orders.domain.entities.order_line_entity import OrderLineEntity


@dataclass
class OrderEntity:
    id: str
    lines: Optional[List[OrderLineEntity]]
    offer_id: str
    offer_name: str
    total: float

    def get_total(self) -> float:
        _total = 0.0

        for line in self.lines:
            _total += line.subtotal

        return _total

    def to_dict(self):
        return {
            "id": self.id,
            "lines": [
                line.to_dict()
                for line in self.lines
            ],
            "offer_id": self.offer_id,
            "offer_name": self.offer_name,
            "total": self.total,
        }
