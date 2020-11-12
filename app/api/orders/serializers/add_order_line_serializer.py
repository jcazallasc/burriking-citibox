from rest_framework import serializers


class AddOrderLineRequest(serializers.Serializer):
    product_id = serializers.UUIDField(required=True)
    product_options = serializers.ListField(required=True, child=serializers.UUIDField())
