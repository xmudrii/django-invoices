from django.shortcuts import render, redirect


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Vezbe 13'})
    else:
        return redirect('invoices_app:invoices')


def invoices(req):
    return None


def invoice(req):
    return None


def new(req):
    return None


def edit(req):
    return None
