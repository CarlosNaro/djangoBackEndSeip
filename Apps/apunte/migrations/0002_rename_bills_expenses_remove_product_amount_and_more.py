# Generated by Django 4.0.6 on 2022-07-05 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apunte', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bills',
            new_name='Expenses',
        ),
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='client',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=3, max_digits=8)),
                ('date', models.DateField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apunte.client')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=8)),
                ('price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apunte.order')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apunte.product')),
            ],
        ),
    ]
