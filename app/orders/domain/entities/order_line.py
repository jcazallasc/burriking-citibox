from dataclasses import dataclass

from orders.domain.entities.product_option import ProductOption


@dataclass
class OrderLine:
    id: str
    product_name: str
    product_base_price: float
    product_options: list[ProductOption] = []
