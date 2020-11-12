import abc


class OrderRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, order_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, order_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def add_order_line(self, order_id: int, order_line_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_order_line(self, order_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_order_lines(self, order_id: int) -> list:
        raise NotImplementedError
