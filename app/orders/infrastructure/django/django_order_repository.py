import json
from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from orders.domain.entities.order_entity import OrderEntity
from orders.domain.entities.order_line_entity import OrderLineEntity
from orders.domain.entities.product_option_entity import ProductOptionEntity
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

    def get_orders_data(self) -> List[OrderEntity]:
        _result = []
        _orders = Order.objects.all()

        for _order in _orders:
            _result.append(self.get_order_data(_order.id))

        return _result

    def get_order_data(self, order_uuid: str) -> OrderEntity:
        try:
            _order = Order.objects.get(id=order_uuid)
        except ObjectDoesNotExist:
            raise OrderDoesNotExist

        _order_lines = []
        for _order_line in _order.order_lines.all():
            _product_options = []
            for _product_option in json.loads(_order_line.product_options):
                _product_options.append(ProductOptionEntity(**_product_option))

            _order_lines.append(
                OrderLineEntity(
                    id=_order_line.id,
                    product_name=_order_line.product_name,
                    product_base_price=_order_line.product_base_price,
                    product_options=_product_options,
                )
            )

        return OrderEntity(
            id=order_uuid,
            lines=_order_lines
        )
