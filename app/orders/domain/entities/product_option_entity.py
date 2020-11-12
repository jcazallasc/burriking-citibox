from dataclasses import dataclass


@dataclass
class ProductOptionEntity:
    label: str
    group: str
    extra_price: float

    def to_dict(self) -> dict:
        return {
            "label": self.label,
            "group": self.group,
            "extra_price": self.extra_price,
        }
