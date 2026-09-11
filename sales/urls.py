from django.urls import path
from .views import CustomerCreateView, ProductCatalogView, ProductDetailView, AddToOrderView, OrderCreateView, OrderDetailView

urlpatterns =[
  path('customer/create/', CustomerCreateView.as_view()),
  path("products/", ProductCatalogView.as_view(), name="product_catalog"),
  path("products/<int:pk>/", ProductDetailView.as_view(),name="product_detail",),
  path("order/create/",OrderCreateView.as_view(),name="order_create",),
  path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
  path("products/<int:pk>/add-to-order/",AddToOrderView.as_view(),name="add_to_order",),
]
