from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Order


def say_hello(request):
    result = Product.objects.filter(unit_price__lt=30).aggregate(
        count=Count("id"), min_price=Min("unit_price")
    )

    return render(request, "hello.html", {"name": "Ahmed", "result": result})
