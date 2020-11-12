from dataclasses import dataclass


@dataclass(frozen=True)
class OrderId:
    value: str
