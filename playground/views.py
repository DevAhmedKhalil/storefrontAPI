from django.shortcuts import render
from store.models import Product, Collection


def say_hello(request):
    # 1) Best way to creatin object
    collection = Collection()
    collection.title = "Video Games"
    collection.featured_product = Product(pk=1)
    # OR
    # collection.featured_product_id = 1
    collection.save()

    # # 2) Using constractor
    # collection = Collection(title="Test Collection", featured_product_id=1)
    # collection.save()

    # 3) Using create method
    # collection = Collection.objects.create(
    #     title="Test Collection", featured_product_id=1
    # )

    return render(request, "hello.html", {"name": "Ahmed"})
