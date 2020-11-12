import uuid

from django.db import models

from .order import Order


class OrderLine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_lines")
    product_id = models.UUIDField()
    product_name = models.CharField(max_length=120)
    product_base_price = models.FloatField()
    product_options = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.product_name} - {self.product_base_price}"
