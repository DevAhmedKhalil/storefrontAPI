from django.shortcuts import render
from django.db.models import Count, Max, Min, Avg, Sum, Value, F, ExpressionWrapper
from django.db.models.fields import DecimalField
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    discounted_price = ExpressionWrapper(
        F("unit_price") * 0.8, output_field=DecimalField()
    )
    queryset = Product.objects.annotate(discounted_price=discounted_price)

    return render(request, "hello.html", {"name": "Ahmed", "result": list(queryset)})
