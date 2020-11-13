from dataclasses import dataclass
from typing import List


@dataclass
class SubproductEntity:
    subproduct_name: str
    subproduct_options: List[dict]

    def to_dict(self) -> dict:
        return {
            "subproduct_name": self.subproduct_name,
            "subproduct_options": self.subproduct_options,
        }
