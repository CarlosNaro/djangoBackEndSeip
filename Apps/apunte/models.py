from django.db import models

# Create your models here.


# tabla producto
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        text = "{0} {1}"
        return text.format(self.name, self.description)


# tabla Cliente
class Client(models.Model):
    name = models.CharField(max_length=250)
    document = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        text = "{0} - {1}"
        return text.format(self.name, self.description)

    # def __str__(self) -> str:
    #     text = "{0} "
    #     return text.format(self.name)


# Tabla Order
class Order(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    subTotal = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )
    total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.id_client.name


# tabla Detail
class Detail(models.Model):
    id_order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_details"
    )
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    subTotal = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    # def suma(self ):
    #     text = "{0}"
    #     return text.format(round(self.amount * self.price ,2))

    # def __str__(self):
    #     text="Nom_Orden: {0} / Product: {1} / Cantidad: {2} / PU: {3} / Total :{4}"
    #     return text.format(self.id_order,self.id_product, self.amount, self.price,self.suma() )


# tabla expenses
class Expenses(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    description = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
