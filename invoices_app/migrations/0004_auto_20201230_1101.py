# Generated by Django 3.1.4 on 2020-12-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_app', '0003_auto_20201230_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]
