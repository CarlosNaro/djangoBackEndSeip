# Generated by Django 4.0.5 on 2022-07-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apunte', '0002_rename_bills_expenses_remove_product_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
