from django.db import models


class Option(models.Model):
    label = models.CharField(max_length=120)
    group = models.CharField(max_length=120)
    extra_price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
