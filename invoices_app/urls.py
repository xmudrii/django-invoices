from django.urls import path
from . import views

app_name = 'invoices_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('invoices/', views.invoices, name='invoices'),
    path('invoice/<int:invoice_id>/', views.invoice, name='invoice'),
    path('invoice/new/', views.invoice_new, name='new'),
    path('invoice/edit/<int:invoice_id>/', views.invoice_edit, name='edit'),
    path('invoice/delete/<int:invoice_id>/', views.invoice_delete, name='delete'),
    path('invoice/<int:invoice_id>/new', views.invoice_new_item, name='new_item'),
    path('invoice/item/edit/<int:item_id>', views.invoice_edit_item, name='edit_item'),
    path('invoice/item/delete/<int:item_id>', views.invoice_delete_item, name='delete_item')
]
