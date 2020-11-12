from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    base_price = models.FloatField(default=0.0)
    stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
