from django.urls import path
from . import views

app_name = 'invoices_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('invoices/', views.invoices, name='invoices'),
    path('invoice/new/', views.invoice_new, name='new'),
    path('invoice/edit/<int:invoice_id>/', views.invoice_edit, name='edit'),
    path('invoice/additem/<int:invoice_id>', views.invoice_add_item, name='additem')
]
