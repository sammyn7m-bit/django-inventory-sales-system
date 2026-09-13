from django.core.exceptions import ValidationError
from django.db import transaction

from inventory.services import sell_stock
from .models import Order


@transaction.atomic
def pay_order(order):
    if order.status == Order.PAID:
        raise ValidationError("This order has already been paid.")

    if order.status == Order.CANCELLED:
        raise ValidationError("A cancelled order cannot be paid.")

    items = list(order.items.select_related("product"))

    if not items:
        raise ValidationError("Cannot pay an empty order.")

    for item in items:
        if item.quantity > item.product.stock_on_hand:
            raise ValidationError(
                f"Insufficient stock for {item.product.name}. "
                f"Available: {item.product.stock_on_hand}."
            )

    for item in items:
        sell_stock(
            item.product,
            item.quantity,
            f"Order #{order.id}",
        )

    order.status = Order.PAID
    order.save(update_fields=["status"])
