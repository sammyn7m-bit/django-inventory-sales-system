from django.contrib import admin
from .models import Customer, Order, OrderItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "address")
    search_fields = ("name", "phone", "email")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    autocomplete_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "order_date", "status")
    list_filter = ("status", "order_date")
    search_fields = ("id", "customer__name", "customer__phone")
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "unit_price")
    search_fields = ("order__id", "product__name", "product__sku")

