from django.contrib import admin, messages
from django.db.models.query import QuerySet
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ["collection"]
    prepopulated_fields = {
        "slug": ["title"],
    }
    search_fields = ["title"]  # Add this line to specify search fields
    # fields = ["title", "slug"]
    # exclude = ["promotions"]  # Opposite of fields
    # readonly_fields = ["title"]
    actions = ["clear_inventory"]
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_filter = ["collection", "last_update", "inventory"]
    list_per_page = 10
    list_select_related = ["collection"]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        return "Low" if product.inventory < 10 else "Ok"

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset):
        # Update the inventory of selected products to 0
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f"{updated_count} products were successfully updated.",
            messages.SUCCESS,
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = [""]
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10


# admin.site.register(models.Collection)
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]
    search_fields = ["title"]

    @admin.display(ordering="products_count")
    def products_count(self, collection):
        return collection.product_set.count()


# ORDER ITEMS => Table to add orders of products
class OrderItemInline(admin.StackedInline):
    # class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ["product"]
    model = models.OrderItem
    extra = 0
    min_num = 1
    max_num = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer"]
    inlines = [OrderItemInline]
    list_display = ["id", "placed_at", "customer"]
