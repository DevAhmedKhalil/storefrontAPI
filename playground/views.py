from django.shortcuts import render
from store.models import Product, Collection


def say_hello(request):
    # # 1) Updating object -> use .get to update only 'title'
    # collection = Collection.objects.get(pk=11)
    # collection.title = "Games"
    # collection.save()

    # 2) Update object using update method
    Collection.objects.filter(pk=11).update(featured_product=None)
    return render(request, "hello.html", {"name": "Ahmed"})
