from django.urls import path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
router.register("carts", views.CartViewSet)
router.register("customers", views.CustomerViewSet)
router.register("orders", views.OrderViewSet)


product_routers = routers.NestedDefaultRouter(router, "products", lookup="product")
product_routers.register("reviews", views.ReviewViewSet, basename="product-reviews")

carts_routers = routers.NestedDefaultRouter(router, "carts", lookup="cart")
carts_routers.register("items", views.CartItemViewSet, basename="cart-items")

# URLConf
urlpatterns = router.urls + product_routers.urls + carts_routers.urls
