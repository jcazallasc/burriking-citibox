from dataclasses import dataclass
from typing import List, Optional

from orders.domain.entities.product_option_entity import ProductOptionEntity
from orders.domain.entities.subproduct_entity import SubproductEntity


@dataclass
class OrderLineEntity:
    id: str
    product_id: str
    product_name: str
    product_base_price: float
    product_options: Optional[List[ProductOptionEntity]]
    subproducts: Optional[List[SubproductEntity]]
    subtotal: float

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_base_price": self.product_base_price,
            "product_options": [
                product_options.to_dict()
                for product_options in self.product_options
            ],
            "subproducts": [
                subproduct.to_dict()
                for subproduct in self.subproducts
            ],
            "subtotal": self.subtotal,
        }
