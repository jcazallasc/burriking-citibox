import uuid
from dataclasses import dataclass

from orders.domain.exceptions.invalid_uuid import InvalidUUID


@dataclass(frozen=True)
class OrderLineUUId:
    value: str

    def __post_init__(self) -> None:
        try:
            uuid.UUID(self.value)
        except ValueError:
            raise InvalidUUID
