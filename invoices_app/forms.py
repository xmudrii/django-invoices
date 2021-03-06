from django.forms import ModelForm, Form
import django.forms as f
from .models import Invoice, InvoiceItem


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'number',
            'date',
            'company_name',
            'company_address',
            'company_city',
            'company_post_code',
            'company_country',
            'payment_account',
            'remarks'
        ]


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = [
            'description',
            'total'
        ]
