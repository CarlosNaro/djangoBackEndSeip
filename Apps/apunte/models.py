from django.db import models

# Create your models here.

#tabla producto 
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()

#tabla Cliente
class Client(models.Model):
    name = models.CharField(max_length=250)
    document = models.CharField(max_length=8, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()

#Tabla Order 
class Order(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=8, decimal_places=3)
    date = models.DateField()

# tabla Detail 
class Detail(models.Model):
    id_product = models.ForeignKey(Product, on_delete= models.CASCADE)
    id_order = models.ForeignKey(Order, on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    price  = models.DecimalField(max_digits=8, decimal_places=3)

#tabla expenses
class Expenses(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    description = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()



# tabla por eliminar 
# class Bills(models.Model):
#     name = models.CharField(max_length=250)
#     price = models.DecimalField(max_digits=8, decimal_places=3)
#     description = models.CharField(max_length=250, null=True, blank=True)
#     date = models.DateField()
#logramos subir nuestro ´primer Proyecto




