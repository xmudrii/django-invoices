from django.urls import path
from . import views

app_name = 'invoices_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('invoices/', views.invoices, name='invoices'),
    path('invoice/<int:id>/', views.invoice, name='invoice'),
    path('invoice/new/', views.new, name='new'),
    path('invoice/edit/<int:id>/', views.edit, name='edit')
]
