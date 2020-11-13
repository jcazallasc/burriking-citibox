from rest_framework import serializers


class ProductOptions(serializers.Serializer):
    product_option_id = serializers.UUIDField(required=True)
    value = serializers.CharField(required=True)


class SubproductSerializer(serializers.Serializer):
    subproduct_id = serializers.UUIDField(required=True)
    subproduct_options = ProductOptions(many=True, required=True)


class AddOrderLineRequest(serializers.Serializer):
    product_id = serializers.UUIDField(required=True)
    product_options = ProductOptions(many=True, required=True)
    subproducts = SubproductSerializer(many=True, required=False)
