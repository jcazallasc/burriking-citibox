from django.contrib import admin

from orders.infrastructure.persistence.django.option import Option
from orders.infrastructure.persistence.django.order import Order
from orders.infrastructure.persistence.django.order_line import OrderLine
from orders.infrastructure.persistence.django.product import Product
from orders.infrastructure.persistence.django.product_option import ProductOptions


admin.site.register(Option)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Product)
admin.site.register(ProductOptions)
