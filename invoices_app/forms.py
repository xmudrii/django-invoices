from django.forms import ModelForm, Form
import django.forms as f
from .models import Invoice


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'number',
            'companyName',
            'companyAddress',
            'companyCity',
            'companyState',
            'companyPostCode',
            'companyCountry',
            'invoiceDescription',
            'invoiceTotal',
            'paymentAccount'
        ]
