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
                          company_name=form.cleaned_data['company_name'],
                          company_address=form.cleaned_data['company_address'],
                          company_city=form.cleaned_data['company_city'],
                          company_post_code=form.cleaned_data['company_post_code'],
                          company_country=form.cleaned_data['company_country'],
                          payment_account=form.cleaned_data['payment_account'],
                          remarks=form.cleaned_data['remarks'],
                          owner=req.user)
            inv.save()
            return redirect('invoices_app:invoices')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = InvoiceForm()
        return render(req, 'new.html', {'form': form})


def edit(req, id):
    inv = Invoice.objects.get(id=id)
    if req.method == 'POST':
        form = InvoiceForm(req.POST, instance=inv)

        if form.is_valid():
            inv = Invoice.objects.get(id=id)
            inv.number = form.cleaned_data['number']
            inv.date = form.cleaned_data['date']
            inv.company_name = form.cleaned_data['company_name']
            inv.company_address = form.cleaned_data['company_address']
            inv.company_city = form.cleaned_data['company_city']
            inv.company_post_code = form.cleaned_data['company_post_code']
            inv.company_country = form.cleaned_data['company_country']
            inv.payment_account = form.cleaned_data['payment_account']
            inv.remarks = form.cleaned_data['remarks']
            inv.save()
            return redirect('invoices_app:invoices')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        form = InvoiceForm(instance=inv)
        return render(req, 'edit.html', {'form': form, 'id': id})
