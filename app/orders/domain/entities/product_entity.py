from dataclasses import dataclass
from typing import List, Optional

from orders.domain.entities.product_option_entity import ProductOptionEntity


@dataclass
class ProductEntity:
    id: str
    parent_id: str
    name: str
    base_price: float
    product_options: Optional[List[ProductOptionEntity]]
    subproducts: Optional[List["ProductEntity"]]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "parent_id": self.parent_id,
            "name": self.name,
            "base_price": self.base_price,
            "product_options": [
                product_option.to_dict()
                for product_option in self.product_options
            ],
            "subproducts": [
                subproduct.to_dict()
                for subproduct in self.subproducts
            ],
        }
