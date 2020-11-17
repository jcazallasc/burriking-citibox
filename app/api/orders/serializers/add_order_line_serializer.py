from rest_framework import serializers


class ProductOptions(serializers.Serializer):
    """
    Serializers for Create Order Line with product options

    It's required
    """

    product_option_id = serializers.UUIDField(required=True)
    value = serializers.CharField(required=True)


class SubproductSerializer(serializers.Serializer):
    """
    Serializers for Create Order Line with subproducts

    It's optional
    """

    subproduct_id = serializers.UUIDField(required=True)
    subproduct_options = ProductOptions(many=True, required=True)


class AddOrderLineRequest(serializers.Serializer):
    """
    Serializer to validad the request for Create Order Line
    """

    product_id = serializers.UUIDField(required=True)
    product_options = ProductOptions(many=True, required=True)
    subproducts = SubproductSerializer(many=True, required=False)
