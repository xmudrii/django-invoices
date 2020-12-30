from django.urls import path
from . import views

app_name = 'invoices_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('invoices/', views.invoices, name='invoices'),
    path('invoice/new/', views.invoice_new, name='new'),
    path('invoice/edit/<int:invoice_id>/', views.invoice_edit, name='edit'),
    path('invoice/delete/<int:invoice_id>/', views.invoice_delete, name='delete'),
    path('invoice/newitem/<int:invoice_id>', views.invoice_new_item, name='newitem'),
    path('invoice/edititem/<int:item_id>', views.invoice_edit_item, name='edititem'),
    path('invoice/deleteitem/<int:item_id>', views.invoice_delete_item, name='deleteitem')
]
