from django.contrib import admin
from .models import Supplier, Product, StockMovement


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email", "phone")


class StockMovementInline(admin.TabularInline):
    model = StockMovement
    extra = 0
    readonly_fields = ("movement_type", "quantity_change", "note")
    can_delete = False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "supplier",
        "cost_price",
        "selling_price",
        "low_stock_threshold",
        "is_active",
    )
    list_filter = ("is_active", "supplier")
    search_fields = ("name", "sku", "description")
    list_editable = ("selling_price", "is_active")
    inlines = [StockMovementInline]


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ("product", "movement_type", "quantity_change", "note")
    list_filter = ("movement_type", "product")
    search_fields = ("product__name", "product__sku", "note")

