from dataclasses import dataclass


@dataclass
class ProductOption:
    id: str
    label: str
    extra_price: float
