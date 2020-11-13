import json
import uuid

from django.db import models

from orders.domain.entities.order_line_entity import OrderLineEntity
from orders.domain.entities.product_option_entity import ProductOptionEntity

from .order import Order


class OrderLine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_lines")
    product_id = models.UUIDField()
    product_name = models.CharField(max_length=120)
    product_base_price = models.FloatField()
    product_options = models.TextField()
    subtotal = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.product_name} - {self.product_base_price}"

    def to_entity(self) -> OrderLineEntity:
        return OrderLineEntity(
            id=str(self.id),
            product_id=self.product_id,
            product_name=self.product_name,
            product_base_price=self.product_base_price,
            product_options=[
                ProductOptionEntity(**product_option)
                for product_option in json.loads(self.product_options)
            ],
            subtotal=self.subtotal,
        )
