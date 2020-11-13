import json
import uuid

from django.db import models

from orders.domain.entities.product_option_entity import ProductOptionEntity

from .product import Product


class ProductOption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_options")
    label = models.CharField(max_length=120)
    values = models.TextField(default=json.dumps([]))
    extra_price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.product.name} - {self.label} - {self.extra_price}"

    def to_entity(self) -> ProductOptionEntity:
        return ProductOptionEntity(
            id=str(self.id),
            label=self.label,
            values=json.loads(self.values),
            extra_price=self.extra_price,
        )
