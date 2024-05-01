from django.shortcuts import render
from store.models import Product, Collection


def say_hello(request):
    # 1) Delete object
    collection = Collection(pk=11)
    collection.delete()

    # 2) Delete object using delete()
    Collection.objects.filter(id__gt=10).delete()

    return render(request, "hello.html", {"name": "Ahmed"})
