from dataclasses import dataclass
from typing import List, Optional

from orders.domain.entities.product_option_entity import ProductOptionEntity


@dataclass
class OrderLineEntity:
    id: str
    product_name: str
    product_base_price: float
    product_options: Optional[List[ProductOptionEntity]]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "product_name": self.product_name,
            "product_base_price": self.product_base_price,
            "product_options": [
                product_options.to_dict()
                for product_options in self.product_options
            ],
        }
