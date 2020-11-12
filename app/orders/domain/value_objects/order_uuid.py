from dataclasses import dataclass


@dataclass(frozen=True)
class OrderUUId:
    value: str
