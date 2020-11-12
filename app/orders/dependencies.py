from orders.infrastructure.django.django_order_repository import DjangoOrderRepository


class Dependencies:

    def __init__(self) -> None:
        self.order_repository = DjangoOrderRepository()


dependencies = Dependencies()
