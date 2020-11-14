from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

from orders.domain.entities.order_line_entity import OrderLineEntity


if TYPE_CHECKING:
    from orders.domain.entities.offer_entity import OfferEntity


@dataclass
class OrderEntity:
    id: str
    lines: Optional[List[OrderLineEntity]]
    offer_id: Optional[str]
    offer_name: Optional[str]
    total: float

    def __str__(self) -> str:
        lines = ", ".join([
            str(line)
            for line in self.lines
        ])

        return f"{lines} {self.total}€"

    def calculate_total(self, offers: List["OfferEntity"]) -> None:
        _total = 0.0

        for _line in self.lines:
            _total += _line.subtotal

        _offers = {_offer.discount: _offer for _offer in offers if _offer.check(self)}

        self.offer_id = None
        self.offer_name = None
        if len(_offers):
            _min_offer_discount = min(set(_offers.keys()))

            self.offer_id = _offers[_min_offer_discount].id
            self.offer_name = _offers[_min_offer_discount].name

            _total -= _total * _min_offer_discount / 100

        self.total = _total

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
