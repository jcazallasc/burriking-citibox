from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.application.list_orders.order_list import OrderList
from orders.dependencies import dependencies


class OrderListAPIView(APIView):

    def get(self, request) -> Response:
        _orders_data = OrderList(dependencies.order_repository).list()

        return Response(_orders_data, status=status.HTTP_200_OK)
