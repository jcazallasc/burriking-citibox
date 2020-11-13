from django.contrib import admin

from orders.infrastructure.persistence.django.offer import Offer
from orders.infrastructure.persistence.django.order import Order
from orders.infrastructure.persistence.django.order_line import OrderLine
from orders.infrastructure.persistence.django.product import Product
from orders.infrastructure.persistence.django.product_option import ProductOption


admin.site.register(Offer)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Product)
admin.site.register(ProductOption)
