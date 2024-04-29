from django.shortcuts import render
from django.db.models import Q
from store.models import Product


def say_hello(request):
    # keyword=value
    # queryset = Product.objects.filter(unit_price__range=(20, 40))
    # queryset = Product.objects.filter(title__icontains="coffee")

    # products: where inventroy < 10 AND units_price < 20
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    # products: where inventroy < 10 OR units_price < 20
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    return render(request, "hello.html", {"name": "Mosh", "products": list(queryset)})
