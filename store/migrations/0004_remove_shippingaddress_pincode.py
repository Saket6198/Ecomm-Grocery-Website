# Generated by Django 4.2.5 on 2023-10-26 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_shippingaddress_state_shippingaddress_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='pincode',
        ),
    ]
