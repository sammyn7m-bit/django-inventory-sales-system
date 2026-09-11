from django.core.exceptions import ValidationError

from inventory.services import sell_stock
from .models import Order


def pay_order(order):
    if order.status == Order.PAID:
        raise ValidationError("This order has already been paid.")

    if order.status == Order.CANCELLED:
        raise ValidationError("A cancelled order cannot be paid.")

    items = order.items.all()

    if not items.exists():
        raise ValidationError("Cannot pay an empty order.")

    for item in items:
        sell_stock(
            item.product,
            item.quantity,
            f"Order #{order.id}"
        )

    order.status = Order.PAID
    order.save(update_fields=["status"])
