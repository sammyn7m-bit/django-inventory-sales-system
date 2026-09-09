from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Supplier, Product
from django.views import generic
from .services import add_stock, sell_stock
from .forms import ProductForm, SupplierForm

# supplier list
class SupplierListView(generic.ListView):
    model = Supplier
    template_name = 'inventory/suppliers_list.html'
    context_object_name = 'suppliers'

# add a supplier
class SupplierCreateView(generic.CreateView):
    form_class = SupplierForm
    template_name = 'inventory/suppliers_create.html'
    success_url = reverse_lazy('supplier_list')

# supplier update/delete
class SupplierUpdate(generic.UpdateView):
    form_class = SupplierForm
    fields = [
        "name",
        "email",
        "phone",
    ]
    template_name = "inventory/suppliers_create.html"
    success_url = reverse_lazy("supplier_list")


class SupplierDelete(generic.DeleteView):
    model = Supplier
    template_name = "inventory/supplier_delete.html"
    success_url = reverse_lazy("supplier_list")

# product list
class ProductListView(generic.ListView):
    model = Product
    template_name = 'inventory/products_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-bought_at')

# To create/add a product
class ProductCreateView(generic.CreateView):
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')

# to views a product detail
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "inventory/product_detail.html"
    context_object_name = "product"

# product update
class ProductUpdate(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')

# product delete
class ProductDelete(generic.DeleteView):
    model = Product
    template_name = 'inventory/product_delete.html'
    success_url = reverse_lazy('product_list')

# when new products bought add to the stock
class AddStockView(generic.View):

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        qty = request.POST.get("qty")
        note = request.POST.get("note", "")

        add_stock(product, qty, note)

        return redirect("product-detail", pk=product.pk)

# reduce stock when a product is sold
class SellStockView(generic.View):

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        qty = request.POST.get("qty")
        note = request.POST.get("note", "")

        sell_stock(product, qty, note)

        return redirect("product-detail", pk=product.pk)
