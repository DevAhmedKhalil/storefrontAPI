from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from pprint import pprint

router = DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)
# pprint(router.urls)

# URLConf
urlpatterns = router.urls

# urlpatterns = [
#     # path("products/", views.ProductList.as_view()),
#     # path("products/<int:pk>/", views.ProductDetail.as_view()),
#     # path("collections/", views.CollectionList.as_view()),
#     # path("collections/<int:pk>/", views.collection_detail, name="collection-detail"),
# ]
