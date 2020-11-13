import abc
from typing import List

from orders.domain.entities.order_entity import OrderEntity


class OrderRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, order_uuid: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, order_uuid: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def create_order_line(
        self,
        order_uuid: str,
        order_line_uuid: str,
        product_uuid: str,
        options: List[dict],
        subproducts: List[dict],
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_order_line(self, order_line_uuid: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_orders_data(self) -> List[OrderEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_order_data(self, order_uuid: str) -> OrderEntity:
        raise NotImplementedError
