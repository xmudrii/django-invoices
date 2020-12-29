from django.db import models
from django.contrib.auth.models import User


class Invoice(models.Model):
    number = models.CharField(max_length=6, db_index=True, unique=True)
    companyName = models.CharField(max_length=50)
    companyAddress = models.CharField(max_length=100)
    companyCity = models.CharField(max_length=50)
    companyState = models.CharField(max_length=50)
    companyPostCode = models.CharField(max_length=5)
    companyCountry = models.CharField(max_length=50)
    invoiceDescription = models.TextField()
    invoiceTotal = models.DecimalField(max_digits=20, decimal_places=3)
    paymentAccount = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.number + ' (' + self.companyName + ")"
