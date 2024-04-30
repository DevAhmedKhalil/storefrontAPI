from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    # Grouping Data:
    # See the number of orders for each customer
    queryset = Customer.objects.annotate(orders_count=Count("order"))

    return render(request, "hello.html", {"name": "Ahmed", "result": list(queryset)})
