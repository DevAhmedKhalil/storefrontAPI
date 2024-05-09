from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title"]

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "unit_price", "price_with_tax", "collection"]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(
    #     max_digits=6, decimal_places=2, source="unit_price"
    # )
    # collection = serializers.HyperlinkedRelatedField(  # Way (4)
    #     queryset=Collection.objects.all(),
    #     view_name="collection-detail",
    # )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
