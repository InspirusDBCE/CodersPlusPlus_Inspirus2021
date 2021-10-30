from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models her
class Item(models.Model):
    name = models.CharField(max_length=100)
    barcode_no = models.IntegerField(null=False, blank=False, unique=True)
    stock_left = models.IntegerField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    cost_price = models.FloatField(null=False, blank=False)
    category = models.CharField(max_length=50)
    expiry_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    margin = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.barcode_no}: {self.stock_left}: {self.selling_price}: {self.cost_price}: {self.expiry_date}: {self.description}: {self.margin}"


class Invoice(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    payment_status = models.BooleanField(null=False, blank=False)
    date = models.DateField(default=datetime.datetime.now, null=False, blank=False)
    total_price = models.FloatField(null=False, blank=False)
    profit = models.FloatField(null=False, blank=False)
    items = models.ManyToManyField(Item, through="Quantity")

    def __str__(self):
        return f"{self.payment_status}: {self.date}: {self.total_price}: {self.profit}"


class Quantity(models.Model):
    item_selected = models.ForeignKey(Item, on_delete=models.CASCADE)
    invoice_selected = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Purchased ({self.item_selected.name}) quantity ({self.quantity})"