# imprtaciones propias 
from Apps.apunte.models import *
from Apps.apunte.serializer import *
from rest_framework.viewsets import ModelViewSet
# create your ViewSets here
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
#:::
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#:::
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
#:::
class DetailViewSet(ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
#:::
class ExpenseViewSet(ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


# class BillsViewSet(ModelViewSet):
#     queryset = Bills.objects.all()
#     serializer_class = BillsSerializer