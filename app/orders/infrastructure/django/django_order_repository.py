import json
from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from orders.domain.entities.order_entity import OrderEntity
from orders.domain.exceptions import (
    OrderAlreadyExist,
    OrderDoesNotExist,
    OrderLineAlreadyExist,
    OrderLineDoesNotExist,
    ProductDoesNotExist,
)
from orders.domain.order_repository import OrderRepository
from orders.infrastructure.persistence.django.order import Order
from orders.infrastructure.persistence.django.order_line import OrderLine
from orders.infrastructure.persistence.django.product import Product
from orders.infrastructure.persistence.django.product_option import ProductOption


class DjangoOrderRepository(OrderRepository):

    def create(self, order_uuid: str) -> None:
        try:
            Order.objects.create(id=order_uuid)
        except IntegrityError:
            raise OrderAlreadyExist

    def delete(self, order_uuid: str) -> None:
        try:
            Order.objects.get(id=order_uuid).delete()
        except ObjectDoesNotExist:
            raise OrderDoesNotExist

    def create_order_line(self, order_uuid: str, order_line_uuid: str, product_uuid: str, options: List[str]) -> None:
        try:
            _product = Product.objects.get(id=product_uuid)
        except ObjectDoesNotExist:
            raise ProductDoesNotExist

        _subtotal = _product.base_price
        _product_options = []

        for _product_option in ProductOption.objects.filter(id__in=options).all():
            _subtotal += _product_option.option.extra_price
            _product_options.append(_product_option.to_entity().to_dict())

        try:
            OrderLine.objects.create(
                id=order_line_uuid,
                order_id=order_uuid,
                product_id=_product.id,
                product_name=_product.name,
                product_base_price=_product.base_price,
                product_options=json.dumps(_product_options),
                subtotal=_subtotal
            )
        except IntegrityError:
            raise OrderLineAlreadyExist

    def delete_order_line(self, order_line_uuid: str) -> None:
        try:
            OrderLine.objects.get(id=order_line_uuid).delete()
        except ObjectDoesNotExist:
            raise OrderLineDoesNotExist

    def get_orders_data(self) -> List[OrderEntity]:
        _result = []
        _orders = Order.objects.all()

        for _order in _orders:
            _result.append(_order.to_entity())

        return _result

    def get_order_data(self, order_uuid: str) -> OrderEntity:
        try:
            return Order.objects.get(id=order_uuid).to_entity()
        except ObjectDoesNotExist:
            raise OrderDoesNotExist
