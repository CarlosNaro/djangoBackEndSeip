from django.db import models

# Create your models here.
#tabla Cliente
class Client(models.Model):
    name = models.CharField(max_length=250)
    document = models.CharField(max_length=8, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()
#tabla Producto
class Product(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=8,decimal_places=3)
    price = models.DecimalField(max_digits=8,decimal_places=3)
    description = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()
#Tabla Gastos 
class Bills(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    description = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()




