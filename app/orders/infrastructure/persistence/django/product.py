import uuid

from django.db import models

from orders.domain.entities.product_entity import ProductEntity


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="subproducts", null=True)
    name = models.CharField(max_length=120)
    base_price = models.FloatField(default=0.0, null=True)
    stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name} - {self.base_price}"

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=str(self.id),
            parent_id=self.parent_id,
            name=self.name,
            base_price=self.base_price,
            product_options=[
                product_option.to_entity()
                for product_option in self.product_options.all()
            ],
            subproducts=[
                subproduct.to_entity()
                for subproduct in self.subproducts.all()
            ],
        )
