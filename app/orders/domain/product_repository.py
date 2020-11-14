import abc

from orders.domain.entities.product_entity import ProductEntity
from orders.domain.entities.product_option_entity import ProductOptionEntity


class ProductRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_product(self, product_uuid: str) -> ProductEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def get_product_option(self, product_option_uuid: str) -> ProductOptionEntity:
        raise NotImplementedError
