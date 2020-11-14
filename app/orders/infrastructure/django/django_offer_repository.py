from typing import List

from orders.domain.entities.offer_entity import OfferEntity
from orders.domain.offer_repository import OfferRepository
from orders.infrastructure.persistence.django.offer import Offer


class DjangoOfferRepository(OfferRepository):

    def get_all(self) -> List[OfferEntity]:
        return [_offer.to_entity() for _offer in Offer.objects.all()]
