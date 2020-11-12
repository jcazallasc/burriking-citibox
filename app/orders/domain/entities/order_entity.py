from dataclasses import dataclass
from typing import List, Optional

from orders.domain.entities.order_line_entity import OrderLineEntity


@dataclass
class OrderEntity:
    id: str
    lines: Optional[List[OrderLineEntity]]

    def get_total(self) -> float:
        _total = 0.0

        for line in self.lines:
            _total += line.product_base_price
            for product_option in line.product_options:
                _total += product_option.extra_price

        return _total

    def to_dict(self):
        return {
            "id": self.id,
            "lines": [
                line.to_dict()
                for line in self.lines
            ],
            "total": self.get_total(),
        }
