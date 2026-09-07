from inventory.models import StockMovement

def add_stock(product, qty, note=""):
    return StockMovement.objects.create(
        product=product,
        movement_type=StockMovement.RECEIPT,
        qty_change=int(qty),   # + adds
        note=note
    )

def sell_stock(product, qty, note=""):
    return StockMovement.objects.create(
        product=product,
        movement_type=StockMovement.SALE,
        qty_change=-int(qty),  # - reduces
        note=note
   )
