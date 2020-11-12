import json
from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from orders.domain.exceptions import OrderAlreadyExist, OrderDoesNotExist, OrderLineAlreadyExist, OrderLineDoesNotExist
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
            _product_options = ProductOption.objects.filter(id__in=options).all()

            _options_to_dump = []
            for _product_option in _product_options:
                _options_to_dump.append({
                    "label": _product_option.option.label,
                    "group": _product_option.option.group,
                    "extra_price": _product_option.option.extra_price
                })

            OrderLine.objects.create(
                id=order_line_uuid,
                order_id=order_uuid,
                product_name=_product.name,
                product_base_price=_product.base_price,
                product_options=json.dumps(_options_to_dump)
            )
        except IntegrityError:
            raise OrderLineAlreadyExist

    def delete_order_line(self, order_line_uuid: str) -> None:
        try:
            OrderLine.objects.get(id=order_line_uuid).delete()
        except ObjectDoesNotExist:
            raise OrderLineDoesNotExist

    def get_order_lines(self, order_uuid: str) -> list:
        OrderLine.objects.filter(order_id=order_uuid).all()
