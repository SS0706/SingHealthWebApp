# Generated by Django 3.1.5 on 2021-02-21 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Directory',
        ),
    ]
