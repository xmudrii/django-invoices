# Generated by Django 3.1.4 on 2020-12-30 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_app', '0004_auto_20201230_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='companyName',
            new_name='company_name',
        ),
    ]