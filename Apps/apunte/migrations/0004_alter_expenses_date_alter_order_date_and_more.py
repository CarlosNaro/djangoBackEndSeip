# Generated by Django 4.0.5 on 2022-09-10 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apunte', '0003_alter_client_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]