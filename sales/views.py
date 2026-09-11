from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib import messages

from .models import Order, Customer, OrderItem
from .services import pay_order
from inventory.models import Product
from .forms import CustomerForm


# get customer details
class CustomerCreateView(generic.CreateView):
    model = Customer
    template_name = "sales/customer_create.html"
    fields = [
        "name",
        "phone",
        "email",
        "address",
    ]


def pay(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        pay_order(order)

    return redirect("order_detail", pk=order.pk)


# show / display / products dashboard
class ProductCatalogView(generic.ListView):
    model = Product
    template_name = "sales/product_catalog.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by("name")


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "sales/product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


# choos3 a product to add to order
class AddToOrderView(generic.View):
    def post(self, request, pk):
        product = get_object_or_404(
            Product,
            pk=pk,
            is_active=True
        )

        quantity = request.POST.get("quantity")

        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            messages.error(request, "Invalid quantity.")
            return redirect("product_detail", pk=product.pk)

        if quantity <= 0:
            messages.error(request, "Quantity must be greater than zero.")
            return redirect("product_detail", pk=product.pk)

        if quantity > product.stock_on_hand:
            messages.error(
                request,
                f"Only {product.stock_on_hand} units are available."
            )
            return redirect("product_detail", pk=product.pk)

        request.session["cart"] = {
            "product_id": product.pk,
            "quantity": quantity,
        }

        messages.success(
            request,
            f"{product.name} added to your order."
        )

        return redirect("order_create")


# place an order
class OrderCreateView(generic.FormView):
    template_name = "sales/order_create.html"
    form_class = CustomerForm

    def form_valid(self, form):
        cart = self.request.session.get("cart")

        if not cart:
            messages.error(self.request, "Your order is empty.")
            return redirect("product_catalog")

        product = get_object_or_404(
            Product,
            pk=cart["product_id"],
            is_active=True
        )

        quantity = cart["quantity"]

        if quantity > product.stock_on_hand:
            messages.error(
                self.request,
                f"Only {product.stock_on_hand} units are available."
            )
            return redirect("product_detail", pk=product.pk)

        customer = form.save()

        order = Order.objects.create(
            buyer=customer
        )

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            unit_price=product.selling_price
        )

        self.request.session.pop("cart", None)

        return redirect("order_detail", pk=order.pk)


# view orders created
class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "sales/order_detail.html"
    context_object_name = "order"
