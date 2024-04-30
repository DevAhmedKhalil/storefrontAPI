from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem, Order


def say_hello(request):
    # # Sorting
    # queryset = Product.objects.order_by("unit_price", "-title").reverse()

    # # Limitization 0, 1, 2, 3, 4
    # queryset = Product.objects.all()[0:5]

    # # Pagenation 5, 6, 7, 8, 9
    # queryset = Product.objects.all()[5:10]

    # Selecting Fields To Query
    # queryset = Product.objects.values("id", "title", "collection__title")
    # orderedProducts = OrderItem.objects.values("product_id").distinct()
    # queryset = Product.objects.filter(id__in=orderedProducts).order_by("title")

    # # Deferring Fields
    # # only -> only use this columns if U didn't it will take a long sql queries
    # queryset = Product.objects.only("id", "title")
    # # defer -> don't use id column if U use it it will take a long sql queries
    # queryset = Product.objects.defer("id")

    # Selecting Related Objects
    # queryset = Product.objects.select_related("collection").all()

    queryset = (
        Order.objects.select_related("customer")
        .prefetch_related("orderitem_set__product")
        .order_by("-placed_at")[:5]
    )

    return render(request, "hello.html", {"name": "Ahmed", "orders": list(queryset)})
