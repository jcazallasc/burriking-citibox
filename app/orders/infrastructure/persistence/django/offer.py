import json
import uuid

from django.db import models

from orders.domain.entities.offer_entity import OfferEntity


class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    conditions = models.TextField()
    discount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name} - {self.discount}"

    def to_entity(self) -> OfferEntity:
        return OfferEntity(
            id=str(self.id),
            name=self.name,
            conditions=json.loads(self.conditions),
            discount=self.discount,
        )
