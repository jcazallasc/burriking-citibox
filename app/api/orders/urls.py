################################################################################
#                HELLOUMI S.L. LLC ("HELLOUMI S.L") CONFIDENTIAL               #
#    Unpublished Copyright (c) 2015-2016 HELLOUMI S.L, All Rights Reserved.    #
################################################################################

from django.urls import path

from api.orders.views.order_line_view import OrderLineAPIView
from api.orders.views.order_list_view import OrderListAPIView
from api.orders.views.order_view import OrderAPIView


app_name = 'api_orders'
urlpatterns = [
    path('', OrderListAPIView.as_view()),
    path('<str:order_uuid>/', OrderAPIView.as_view()),
    path('<str:order_uuid>/<str:order_line_uuid>/', OrderLineAPIView.as_view()),
]
