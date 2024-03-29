import json
from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from orders.domain.entities.order_entity import OrderEntity
from orders.domain.exceptions import OrderAlreadyExist, OrderDoesNotExist, OrderLineAlreadyExist, OrderLineDoesNotExist
from orders.domain.offer_repository import OfferRepository
from orders.domain.order_repository import OrderRepository
from orders.domain.product_repository import ProductRepository
from orders.infrastructure.persistence.django.order import Order
from orders.infrastructure.persistence.django.order_line import OrderLine


class DjangoOrderRepository(OrderRepository):

    def __init__(self, offer_repository: OfferRepository, product_repository: ProductRepository) -> None:
        self.offer_repositiory = offer_repository
        self.product_repositiory = product_repository

    def __get_order(self, order_uuid: str) -> Order:
        try:
            return Order.objects.get(id=order_uuid)
        except ObjectDoesNotExist:
            raise OrderDoesNotExist

    def __get_order_line(self, order_line_uuid: str) -> OrderLine:
        try:
            return OrderLine.objects.get(id=order_line_uuid)
        except ObjectDoesNotExist:
            raise OrderLineDoesNotExist

    def __process_total_order(self, order: Order) -> None:
        _order_entity = order.to_entity()
        _offers = self.offer_repositiory.get_all()
        _order_entity.calculate_total(_offers)

        order.total = _order_entity.total
        order.offer_id = _order_entity.offer_id
        order.offer_name = _order_entity.offer_name

        order.save()

    def __get_product_options(self, options: List[dict]) -> List[dict]:
        _product_options = []

        for option in options:
            _product_option = self.product_repositiory.get_product_option(option["product_option_id"])
            _product_options.append({
                **_product_option.to_dict(),
                "value": option["value"],
            })

        return _product_options

    def __get_subproducts(self, subproducts: List[dict]) -> List[dict]:
        _subproducts = []

        for subproduct in subproducts:
            _subproduct = self.product_repositiory.get_product(subproduct["subproduct_id"])

            _data = {
                "subproduct_name": _subproduct.name,
                "subproduct_options": []
            }

            for subproduct_option in subproduct["subproduct_options"]:
                _product_option = self.product_repositiory.get_product_option(subproduct_option["product_option_id"])
                _data["subproduct_options"].append({
                    **_product_option.to_dict(),
                    "value": subproduct_option["value"],
                })

            _subproducts.append(_data)

        return _subproducts

    def __get_subtotal(self, base_price: float, options: List[dict], subproducts: List[dict]) -> float:
        _subtotal = base_price

        for option in options:
            _subtotal += option["extra_price"]

        for subproduct in subproducts:
            for subproduct_option in subproduct["subproduct_options"]:
                _subtotal += subproduct_option["extra_price"]

        return _subtotal

    def create(self, order_uuid: str) -> None:
        try:
            Order.objects.create(id=order_uuid)
        except IntegrityError:
            raise OrderAlreadyExist

    def delete(self, order_uuid: str) -> None:
        self.__get_order(order_uuid).delete()

    def create_order_line(
            self,
            order_uuid: str,
            order_line_uuid: str,
            product_uuid: str,
            options: List[dict],
            subproducts: List[dict],
    ) -> None:
        _product = self.product_repositiory.get_product(product_uuid)
        _product_options = self.__get_product_options(options)
        _subproducts = self.__get_subproducts(subproducts)
        _subtotal = self.__get_subtotal(_product.base_price, _product_options, _subproducts)

        try:
            order_line = OrderLine.objects.create(
                id=order_line_uuid,
                order_id=order_uuid,
                product_id=_product.id,
                product_name=_product.name,
                product_base_price=_product.base_price,
                product_options=json.dumps(_product_options),
                subproducts=json.dumps(_subproducts),
                subtotal=_subtotal
            )
        except IntegrityError:
            raise OrderLineAlreadyExist

        self.__process_total_order(order_line.order)

    def delete_order_line(self, order_line_uuid: str) -> None:
        _order_line = self.__get_order_line(order_line_uuid)
        _order = _order_line.order

        _order_line.delete()

        self.__process_total_order(_order)

    def get_orders_data(self) -> List[OrderEntity]:
        _result = []
        _orders = Order.objects.all()

        for _order in _orders:
            _result.append(_order.to_entity())

        return _result

    def get_order_data(self, order_uuid: str) -> OrderEntity:
        self.__get_order(order_uuid).to_entity()
