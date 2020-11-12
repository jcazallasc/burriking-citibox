import uuid

from django.db import models

from .option import Option
from .product import Product


class ProductOptions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=120)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_options")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="options")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
