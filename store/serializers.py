from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    # collection = serializers.PrimaryKeyRelatedField( # Way (1) it returns the ID of the collection
    #     queryset=Collection.objects.all(),
    # )
    # collection = serializers.StringRelatedField()    # Way (2)
    # collection = CollectionSerializer()              # Way (3)
    collection = serializers.HyperlinkedRelatedField(  # Way (4)
        queryset=Collection.objects.all(),
        view_name="collection-detail",
    )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
