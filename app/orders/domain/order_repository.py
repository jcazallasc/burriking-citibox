import abc
import uuid
from typing import List


class OrderRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, order_uuid: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, order_uuid: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def create_order_line(self, order_uuid: str, order_line_uuid: str, product_uuid: str, options: List[str]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_order_line(self, order_line_uuid: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_order_lines(self, order_uuid: str) -> list:
        raise NotImplementedError
