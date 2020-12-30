import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User


class Invoice(models.Model):
    number = models.CharField(max_length=6, db_index=True, unique=True)
    date = models.DateField(default=django.utils.timezone.now)
    company_name = models.CharField(max_length=50)
    company_address = models.CharField(max_length=100)
    company_city = models.CharField(max_length=50)
    company_post_code = models.CharField(max_length=5)
    company_country = models.CharField(max_length=50)
    payment_account = models.CharField(max_length=25, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number + ' (' + self.company_name + ")"


class InvoiceItem(models.Model):
    description = models.TextField()
    total = models.DecimalField(max_digits=15, decimal_places=2)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description
