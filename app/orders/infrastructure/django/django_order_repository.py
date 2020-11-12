import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from orders.domain.exceptions import OrderAlreadyExist, OrderDoesNotExist, OrderLineAlreadyExist, OrderLineDoesNotExist
from orders.domain.order_repository import OrderRepository
from orders.infrastructure.persistence.django.order import Order
from orders.infrastructure.persistence.django.order_line import OrderLine


class DjangoOrderRepository(OrderRepository):

    def create(self, order_uuid: uuid.UUID) -> None:
        try:
            Order.objects.create(id=order_uuid)
        except IntegrityError:
            raise OrderAlreadyExist

    def delete(self, order_uuid: uuid.UUID) -> None:
        try:
            Order.objects.get(id=order_uuid).delete()
        except ObjectDoesNotExist:
            raise OrderDoesNotExist

    def add_order_line(self, order_uuid: uuid.UUID, order_line_uuid: uuid.UUID) -> None:
        try:
            Order.objects.get(id=order_uuid).order_lines.create(id=order_line_uuid)
        except IntegrityError:
            raise OrderLineAlreadyExist

    def delete_order_line(self, order_line_uuid: uuid.UUID) -> None:
        try:
            OrderLine.objects.get(id=order_line_uuid).delete()
        except ObjectDoesNotExist:
            raise OrderLineDoesNotExist

    def get_order_lines(self, order_uuid: uuid.UUID) -> list:
        return []
