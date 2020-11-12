from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class OrderLineAPIView(APIView):

    def post(self, request, order_uuid: int, order_line_uuid: int) -> Response:
        return Response({}, status=status.HTTP_201_CREATED)

    def delete(self, request, order_uuid: int, order_line_uuid: int) -> Response:
        return Response({}, status=status.HTTP_200_OK)
