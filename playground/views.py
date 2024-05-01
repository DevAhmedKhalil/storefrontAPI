from django.shortcuts import render
from django.db import transaction, connection
from store.models import Product, Collection, Order, OrderItem


def say_hello(request):
    # # Executing Raw SQL Queries
    # # 1) Using objects.raw() method
    # queryset = Product.objects.raw("SELECT id, title FROM store_product")

    # # 2) Using connection module
    # cursor = connection.cursor
    # cursor.execute("SELECT id, title FROM store_product")
    # cursor.close()  # use try finlly block

    # 3) Using connection and 'with as' statement
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title FROM store_product")
        # cursor.callproc("get_customers", [1, 2])

    return render(request, "hello.html", {"name": "Ahmed"})
