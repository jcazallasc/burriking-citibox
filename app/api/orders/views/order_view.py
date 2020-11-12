from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.application.create_order.order_creator import OrderCreator
from orders.application.delete_order.order_deleter import OrderDeleter
from orders.application.get_order.order_getter import OrderGetter
from orders.dependencies import dependencies


class OrderAPIView(APIView):

    def get(self, request, order_uuid: str) -> Response:
        _order_data = OrderGetter(dependencies.order_repository).get_order_data(order_uuid)

        return Response(_order_data, status=status.HTTP_201_CREATED)

    def post(self, request, order_uuid: str) -> Response:
        OrderCreator(dependencies.order_repository).create(order_uuid)

        return Response({}, status=status.HTTP_201_CREATED)

    def delete(self, request, order_uuid: str) -> Response:
        OrderDeleter(dependencies.order_repository).delete(order_uuid)

        return Response({}, status=status.HTTP_200_OK)
