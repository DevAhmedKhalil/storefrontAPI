from django.urls import path

# from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)

product_routers = routers.NestedDefaultRouter(router, "products", lookup="product")
product_routers.register("reviews", views.ReviewViewSet, basename="product-reviews")


# URLConf
urlpatterns = router.urls + product_routers.urls

# urlpatterns = [
#     # path("products/", views.ProductList.as_view()),
#     # path("products/<int:pk>/", views.ProductDetail.as_view()),
#     # path("collections/", views.CollectionList.as_view()),
#     # path("collections/<int:pk>/", views.collection_detail, name="collection-detail"),
# ]
