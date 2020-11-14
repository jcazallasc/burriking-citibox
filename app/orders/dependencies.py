from orders.infrastructure.django.django_offer_repository import DjangoOfferRepository
from orders.infrastructure.django.django_order_repository import DjangoOrderRepository
from orders.infrastructure.django.django_product_repository import DjangoProductRepository


class Dependencies:

    def __init__(self) -> None:
        self.offer_repository = DjangoOfferRepository()
        self.product_repository = DjangoProductRepository()

        self.order_repository = DjangoOrderRepository(
            offer_repository=self.offer_repository,
            product_repository=self.product_repository,
        )


dependencies = Dependencies()
