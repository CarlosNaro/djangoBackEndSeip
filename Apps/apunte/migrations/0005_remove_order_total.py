# Generated by Django 4.0.5 on 2022-09-17 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apunte', '0004_alter_expenses_date_alter_order_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
