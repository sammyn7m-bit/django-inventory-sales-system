import logging

import requests
from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from .forms import ProductForm, SupplierForm
from .models import Product, Supplier
from .openinary import create_upload_signature
from .services import add_stock, sell_stock

logger = logging.getLogger(__name__)



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
    queryset = Supplier.objects.all()
    #form_class = SupplierForm
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


@require_POST
def openinary_sign(request):
    # Origin check, not authentication.
    fetch_site = request.headers.get("Sec-Fetch-Site")

    if fetch_site not in ("same-origin", "same-site"):
        return JsonResponse(
            {"error": "Invalid request origin."},
            status=403,
        )

    # TODO: Require an authenticated and authorized user
    # once authentication is implemented.

    try:
        signature = create_upload_signature()

        return JsonResponse(signature)

    except ImproperlyConfigured:
        logger.exception("Openinary API key is missing.")
        return JsonResponse(
            {"error": "Image upload service is not configured."},
            status=503,
        )

    except requests.RequestException:
        logger.exception("Openinary signing request failed.")
        return JsonResponse(
            {"error": "Could not prepare image upload."},
            status=502,
        )

    except (RuntimeError, KeyError, ValueError):
        logger.exception("Invalid Openinary signing response.")
        return JsonResponse(
            {"error": "Invalid response from image storage."},
            status=502,
        )
