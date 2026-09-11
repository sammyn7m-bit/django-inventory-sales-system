from django.db import models
from inventory.models import Product


class Customer(models.Model):
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 20)
    email = models.EmailField(null = True, blank = True)
    address = models.CharField(max_length = 255, blank = True)

    def __str__(self):
        return self.name

class Order(models.Model):

    DRAFT = "draft"
    PAID = "paid"
    CANCELLED = "cancelled"

    STATUS_CHOICES =[
        (DRAFT,"draft"),
        (PAID, "paid"),
        (CANCELLED, "cancelled"),]

    buyer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="orders")
    order_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return f"{self.buyer} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="order_items"
    )
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return f"{self.product} x {self.quantity} (Order {self.order_id})"


