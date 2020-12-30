from django.forms import ModelForm, Form
import django.forms as f
from .models import Invoice


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'number',
            'date',
            'companyName',
            'companyAddress',
            'companyCity',
            'companyPostCode',
            'companyCountry',
            'paymentAccount',
            'remarks'
        ]
