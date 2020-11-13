from dataclasses import dataclass

from orders.domain.entities.order_entity import OrderEntity
from orders.domain.offers.combine_checker import CombineChecker
from orders.domain.offers.days_of_week_checker import DaysOfWeekChecker


OFFER_CHECKER_MAP = {
    "days_of_week": DaysOfWeekChecker,
    "combine": CombineChecker,
}


@dataclass
class OfferEntity:
    id: str
    name: str
    conditions: dict
    discount: int

    def check(self, order: OrderEntity) -> bool:
        for _condition_key, _condition_value in self.conditions.items():
            if _condition_key not in OFFER_CHECKER_MAP or\
                    not OFFER_CHECKER_MAP[_condition_key](_condition_value, order).check():
                return False

        return True
