from django.db import models
from django.db.models import Sum


class Supplier(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(unique = True, null = True, blank = True)
    phone = models.CharField(max_length = 20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length = 200)
    sku = models.CharField(max_length = 100,unique = True, verbose_name = 'stock keeping unit')
    cost_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    selling_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    low_stock_threshold = models.PositiveIntegerField(default = 5)
    description = models.TextField(blank = True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name="products")
    is_active = models.BooleanField(default=True)
    bought_at = models.DateTimeField(auto_now_add = True)

    @property
    def stock_on_hand(self):
        return self.movements.aggregate(total=Sum("qty_change"))["total"] or 0

    def __str__(self):
        return f"{self.name} ({self.sku})"

class StockMovement(models.Model):
    RECEIPT = "RECEIPT"
    SALE = "SALE"
    ADJUSTMENT = "ADJUSTMENT"

    TYPES =[
     (RECEIPT, "Receipt"),
     (SALE, "Sale"),
     (ADJUSTMENT, "Adjustment"),]

    product = models.ForeignKey(Product,
              on_delete=models.CASCADE,
              related_name="movements")

    movement_date = models.DateTimeField(auto_now_add=True)

    movement_type = models.CharField(max_length=20, choices=TYPES)

    qty_change = models.IntegerField()

    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.product.sku} {self.movement_type} {self.qty_change}"

