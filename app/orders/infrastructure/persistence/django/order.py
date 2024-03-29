import uuid

from django.db import models

from orders.domain.entities.order_entity import OrderEntity


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total = models.FloatField(default=0.0)
    offer_id = models.UUIDField(null=True, blank=True)
    offer_name = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.to_entity())

    def to_entity(self) -> OrderEntity:
        return OrderEntity(
            id=str(self.id),
            lines=[
                line.to_entity()
                for line in self.order_lines.all()
            ],
            offer_id=str(self.offer_id) if self.offer_id else None,
            offer_name=self.offer_name,
            total=self.total,
            created_at=self.created_at,
        )
