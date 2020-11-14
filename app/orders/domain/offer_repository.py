import abc
from typing import List

from orders.domain.entities.offer_entity import OfferEntity


class OfferRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_all(self) -> List[OfferEntity]:
        raise NotImplementedError
