from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.orders.serializers.add_order_line_serializer import AddOrderLineRequest
from orders.application.create_order_line.order_line_creator import OrderLineCreator
from orders.application.delete_order_line.order_line_deleter import OrderLineDeleter
from orders.dependencies import dependencies


class OrderLineAPIView(APIView):

    def post(self, request, order_uuid: int, order_line_uuid: int) -> Response:
        add_order_line_request = AddOrderLineRequest(data=request.data)
        if not add_order_line_request.is_valid():
            return Response(
                add_order_line_request.errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        OrderLineCreator(dependencies.order_repository).create(
            order_uuid,
            order_line_uuid,
            request.data["product_id"],
            request.data["product_options"],
        )

        return Response({}, status=status.HTTP_201_CREATED)

    def delete(self, request, order_uuid: int, order_line_uuid: int) -> Response:
        OrderLineDeleter(dependencies.order_repository).delete(order_line_uuid)

        return Response({}, status=status.HTTP_200_OK)
