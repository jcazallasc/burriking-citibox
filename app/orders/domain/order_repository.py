import abc
import uuid


class OrderRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, order_uuid: uuid.UUID) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, order_uuid: uuid.UUID) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def add_order_line(self, order_uuid: uuid.UUID, order_line_uuid: uuid.UUID) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_order_line(self, order_uuid: uuid.UUID) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_order_lines(self, order_uuid: uuid.UUID) -> list:
        raise NotImplementedError
