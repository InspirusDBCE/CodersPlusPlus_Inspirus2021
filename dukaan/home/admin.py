from django.contrib import admin
from .models import Invoice, Item, Quantity

# Register your models here.
admin.site.register(Invoice)
admin.site.register(Item)
admin.site.register(Quantity)