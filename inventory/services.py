from django.core.exceptions import ValidationError

from inventory.models import StockMovement


def add_stock(product, qty, note=""):
    try:
        qty = int(qty)
    except (TypeError, ValueError):
        raise ValidationError("Quantity must be a valid number.")

    if qty <= 0:
        raise ValidationError("Stock quantity must be greater than zero.")

    return StockMovement.objects.create(
        product=product,
        movement_type=StockMovement.RECEIPT,
        qty_change=qty,
        note=note,
    )


def sell_stock(product, qty, note=""):
    try:
        qty = int(qty)
    except (TypeError, ValueError):
        raise ValidationError("Quantity must be a valid number.")

    if qty <= 0:
        raise ValidationError("Sale quantity must be greater than zero.")

    current_stock = product.stock_on_hand

    if qty > current_stock:
        raise ValidationError(
            f"Insufficient stock. Available stock: {current_stock}."
        )

    return StockMovement.objects.create(
        product=product,
        movement_type=StockMovement.SALE,
        qty_change=-qty,
        note=note,
    )
