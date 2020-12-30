from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Invoices'})
    else:
        return redirect('invoices_app:invoices')


@login_required
def invoices(req):
    inv = Invoice.objects.all()
    return render(req, 'invoices.html', {'invoices': inv})


@login_required
def invoice(req):
    return None


@permission_required('invoices_app.add_invoice')
def invoice_new(req):
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
            return redirect('invoices_app:edit', invoice_id=inv.id)
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = InvoiceForm()
        return render(req, 'new.html', {'form': form})


@permission_required('invoices_app.change_invoice')
def invoice_edit(req, invoice_id):
    inv = get_object_or_404(Invoice, id=invoice_id)
    inv_items = InvoiceItem.objects.filter(invoice=inv)

    if req.method == 'POST':
        form = InvoiceForm(req.POST, instance=inv)

        if form.is_valid():
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
            return render(req, 'edit.html', {'form': form, 'id': invoice_id, 'items': inv_items})
    else:
        form = InvoiceForm(instance=inv)
        return render(req, 'edit.html', {'form': form, 'id': invoice_id, 'items': inv_items})


@permission_required('invoices_app.delete_invoice')
def invoice_delete(req, invoice_id):
    inv = get_object_or_404(Invoice, id=invoice_id)
    inv.delete()
    return redirect('invoices_app:invoices')


@permission_required('invoices_app.change_invoice')
def invoice_new_item(req, invoice_id):
    if req.method == 'POST':
        inv = get_object_or_404(Invoice, id=invoice_id)
        form = InvoiceItemForm(req.POST)

        if form.is_valid():
            invItm = InvoiceItem(description=form.cleaned_data['description'],
                                 total=form.cleaned_data['total'],
                                 invoice=inv,
                                 owner=req.user)
            invItm.save()
            return redirect('invoices_app:edit', invoice_id=invoice_id)
        else:
            return render(req, 'newitem.html', {'form': form, 'invoice_id': invoice_id})
    else:
        form = InvoiceItemForm()
        return render(req, 'newitem.html', {'form': form, 'invoice_id': invoice_id})


@permission_required('invoices_app.change_invoice')
def invoice_edit_item(req, item_id):
    inv_item = get_object_or_404(InvoiceItem, id=item_id)

    if req.method == 'POST':
        form = InvoiceItemForm(req.POST, instance=inv_item)

        if form.is_valid():
            inv_item.description = form.cleaned_data['description']
            inv_item.total = form.cleaned_data['total']
            inv_item.save()
            return redirect('invoices_app:edit', invoice_id=inv_item.invoice.id)
        else:
            return render(req, 'edititem.html', {'form': form, 'item_id': item_id})
    else:
        form = InvoiceItemForm(instance=inv_item)
        return render(req, 'edititem.html', {'form': form, 'item_id': item_id})


@permission_required('invoices_app.change_invoice')
def invoice_delete_item(req, item_id):
    inv_item = get_object_or_404(InvoiceItem, id=item_id)
    inv_item.delete()
    return redirect('invoices_app:edit', invoice_id=inv_item.invoice.id)
