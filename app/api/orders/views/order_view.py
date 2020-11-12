from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.application.create_order.order_creator import OrderCreator
from orders.application.delete_order.order_deleter import OrderDeleter
from orders.dependencies import dependencies


class OrderAPIView(APIView):

    def post(self, request, order_id: int) -> Response:
        OrderCreator(dependencies.order_repository).create(order_id)

        return Response({}, status=status.HTTP_201_CREATED)

    def delete(self, request, order_id: int) -> Response:
        OrderDeleter(dependencies.order_repository).delete(order_id)

        return Response({}, status=status.HTTP_200_OK)
