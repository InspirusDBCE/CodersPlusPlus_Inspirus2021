from django import forms
from .models import Invoice, Item
import datetime

class UFDI(forms.DateInput):
    input_type = 'date'

class InvoiceForm(forms.ModelForm):
    # user = forms.Cha
    payment_status = forms.BooleanField()
    date = forms.DateField(required=False, widget=UFDI(attrs={'min': datetime.datetime.now().date}))
    total_price = forms.FloatField(required=False)
    profit = forms.FloatField(required=False)

    class Meta:
        model = Invoice
        fields = ['payment_status', 'date', 'total_price', 'profit']

class ItemForm(forms.ModelForm):
    name = forms.CharField(required=True)
    barcode_no = forms.FloatField(required=True)
    stock_left = forms.IntegerField(required=True, label='Quantity')
    selling_price = forms.FloatField(required=True)
    cost_price = forms.FloatField(required=True)
    category = forms.CharField(required=True)
    expiry_date = forms.DateField(widget=UFDI(), required=True)
    description = forms.CharField(required=False)
    margin = forms.FloatField(required=False)

    class Meta:
        model = Item
        fields = ['name', 'barcode_no', 'stock_left', 'selling_price', 'cost_price', 'category', 'expiry_date', 'description', 'margin']
