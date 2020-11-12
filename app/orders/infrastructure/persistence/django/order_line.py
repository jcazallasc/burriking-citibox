from django.db import models

from .order import Order


class OrderLine(models.Model):
    product = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_lines")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
