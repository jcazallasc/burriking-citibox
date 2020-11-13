from dataclasses import dataclass
from typing import Optional


@dataclass
class ProductOptionEntity:
    id: str
    label: str
    values: Optional[list]
    extra_price: float
    value: Optional[str] = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "label": self.label,
            "values": self.values,
            "extra_price": self.extra_price,
            "value": self.value,
        }
