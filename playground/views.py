from django.shortcuts import render
from django.db import transaction
from store.models import Product, Collection, Order, OrderItem


def say_hello(request):
    with transaction.atomic():
        # Parent Record
        order = Order()
        order.customer_id = 1
        order.save()

        # Child Record
        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()

    return render(request, "hello.html", {"name": "Ahmed"})
