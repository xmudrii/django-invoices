from django.urls import path
from . import views

app_name = 'invoices_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('invoices/', views.invoices, name='invoices'),
    path('invoice/edit/<int:id>/', views.edit, name='edit'),
    path('invoice/new/', views.new, name='new')
]
