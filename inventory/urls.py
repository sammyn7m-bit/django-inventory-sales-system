from django.urls import path
from .views import ProductListView,ProductCreateView,SupplierCreateView, ProductDetailView, ProductUpdate, ProductDelete, SupplierListView,AddStockView, SellStockView, SupplierUpdate, SupplierDelete

urlpatterns =[
    path('products/', ProductListView.as_view(), name = 'product_list'),
    path('product/create/', ProductCreateView.as_view(), name = 'product_create'),

    path("products/<int:pk>/edit/",ProductUpdate.as_view(),name="product_update",),
    path("products/<int:pk>/delete/",ProductDelete.as_view(),name="product_delete",),

    path('supplier/', SupplierListView.as_view(), name = 'supplier_list'),
    path('supplier/create/', SupplierCreateView.as_view(), name = 'supplier_create'),

    path("suppliers/<int:pk>/edit/", SupplierUpdate.as_view(),name="supplier_update",),

    path("suppliers/<int:pk>/delete/",SupplierDelete.as_view(),name="supplier_delete",),

    path("products<int:pk>/",ProductDetailView.as_view(), name = 'product-detail'),

    path("products/<int:pk>/sell_stock/",SellStockView.as_view(), name="sell_stock"),
    path("products/<int:pk>/add_stock/",AddStockView.as_view(), name="add-stock"),
]
