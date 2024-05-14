from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .models import Product, Collection, OrderItem
from .serializers import ProductSerializer, CollectionSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class ProductDetail(RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response(
                {"Error": "Can Not Delete This product, has order items."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(products_count=Count("products")).all()
    serializer_class = CollectionSerializer


class CollectionDetails(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.annotate(products_count=Count("products")).all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response(
                {"Error": "Can Not Delete This collection, has products."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
