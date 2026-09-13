from django.urls import path

from .views import (
    CustomerCreateView,
    ProductCatalogView,
    ProductDetailView,
    AddToOrderView,
    OrderCreateView,
    OrderDetailView,
    pay,
)

urlpatterns = [
    path(
        "customer/create/",
        CustomerCreateView.as_view(),
        name="customer_create",
    ),
    path(
        "",
        ProductCatalogView.as_view(),
        name="product_catalog",
    ),
    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "products/<int:pk>/add-to-order/",
        AddToOrderView.as_view(),
        name="add_to_order",
    ),
    path(
        "order/create/",
        OrderCreateView.as_view(),
        name="order_create",
    ),
    path(
        "orders/<int:pk>/",
        OrderDetailView.as_view(),
        name="order_detail",
    ),
    path(
        "orders/<int:order_id>/pay/",
        pay,
        name="pay_order",
    ),
]
