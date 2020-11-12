################################################################################
#                HELLOUMI S.L. LLC ("HELLOUMI S.L") CONFIDENTIAL               #
#    Unpublished Copyright (c) 2015-2016 HELLOUMI S.L, All Rights Reserved.    #
################################################################################

from django.urls import path

from api.orders.views.order_line_view import OrderLineAPIView
from api.orders.views.order_view import OrderAPIView


app_name = 'api_orders'
urlpatterns = [
    path('<int:order_id>/', OrderAPIView.as_view()),
    path('<int:order_id>/<int:order_line_id>/', OrderLineAPIView.as_view()), i
]
