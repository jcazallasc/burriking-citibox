from django.core.exceptions import ObjectDoesNotExist

from orders.domain.entities.product_entity import ProductEntity
from orders.domain.entities.product_option_entity import ProductOptionEntity
from orders.domain.exceptions import ProductDoesNotExist, ProductOptionDoesNotExist
from orders.domain.product_repository import ProductRepository
from orders.infrastructure.persistence.django.product import Product
from orders.infrastructure.persistence.django.product_option import ProductOption


class DjangoProductRepository(ProductRepository):

    def get_product(self, product_uuid: str) -> ProductEntity:
        try:
            return Product.objects.get(id=product_uuid).to_entity()
        except ObjectDoesNotExist:
            raise ProductDoesNotExist

    def get_product_option(self, product_option_uuid: str) -> ProductOptionEntity:
        try:
            return ProductOption.objects.get(id=product_option_uuid).to_entity()
        except ObjectDoesNotExist:
            raise ProductOptionDoesNotExist
