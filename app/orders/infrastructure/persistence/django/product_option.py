import uuid

from django.db import models

from orders.domain.entities.product_option_entity import ProductOptionEntity

from .option import Option
from .product import Product


class ProductOption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_options")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="options")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.product.name} - {self.option.label} - {self.option.extra_price}"

    def to_entity(self) -> ProductOptionEntity:
        return ProductOptionEntity(
            id=str(self.id),
            label=self.option.label,
            group=self.option.group,
            extra_price=self.option.extra_price,
        )
