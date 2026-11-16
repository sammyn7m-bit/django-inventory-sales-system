from django.urls import path

from .views import (
    AddStockView,
    ProductCreateView,
    ProductDelete,
    ProductDetailView,
    ProductListView,
    ProductUpdate,
    SellStockView,
    SupplierCreateView,
    SupplierDelete,
    SupplierListView,
    SupplierUpdate,
    openinary_sign,
)

# inventory endpoints
urlpatterns =[
    path('products/', ProductListView.as_view(), name = 'product_list'),
    path('product/create/', ProductCreateView.as_view(), name = 'product_create'),

    path("<int:pk>/edit/",ProductUpdate.as_view(),name="product_update",),
    path("<int:pk>/delete/",ProductDelete.as_view(),name="product_delete",),

    path('suppliers/', SupplierListView.as_view(), name = 'supplier_list'),
    path('supplier/create/', SupplierCreateView.as_view(), name = 'supplier_create'),

    path("suppliers/<int:pk>/edit/", SupplierUpdate.as_view(),name="supplier_update",),

    path("suppliers/<int:pk>/delete/",SupplierDelete.as_view(),name="supplier_delete",),

    path("<int:pk>/",ProductDetailView.as_view(), name = 'product-detail'),

    path("<int:pk>/sell_stock/",SellStockView.as_view(), name="sell_stock"),
    path("products/<int:pk>/add_stock/",AddStockView.as_view(), name="add-stock"),

    # openinary endpoints
    path("openinary/sign/", openinary_sign, name="openinary_sign"),
]
