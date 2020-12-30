from django.shortcuts import render, redirect
from .models import Invoice
from .forms import InvoiceForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Invoices'})
    else:
        return redirect('invoices_app:invoices')


def invoices(req):
    inv = Invoice.objects.all()
    return render(req, 'invoices.html', {'invoices': inv})


def invoice(req):
    return None


def new(req):
    if req.method == 'POST':
        form = InvoiceForm(req.POST)

        if form.is_valid():
            inv = Invoice(number=form.cleaned_data['number'],
                          date=form.cleaned_data['date'],
                          companyName=form.cleaned_data['companyName'],
                          companyAddress=form.cleaned_data['companyAddress'],
                          companyCity=form.cleaned_data['companyCity'],
                          companyPostCode=form.cleaned_data['companyPostCode'],
                          companyCountry=form.cleaned_data['companyCountry'],
                          paymentAccount=form.cleaned_data['paymentAccount'],
                          remarks=form.cleaned_data['remarks'],
                          owner=req.user)
            inv.save()
            return redirect('invoices_app:invoices')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = InvoiceForm()
        return render(req, 'new.html', {'form': form})


def edit(req):
    return None
