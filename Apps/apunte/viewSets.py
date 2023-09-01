# imprtaciones propias 
from rest_framework.response import Response
from rest_framework import status

from Apps.apunte.models import *
from Apps.apunte.serializer import *
from rest_framework.viewsets import ModelViewSet
# create your ViewSets here
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
#:::
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter( isDelete=False )
    serializer_class = ProductSerializer
    #sobre escribir el metodo delete para que no se elimine el producto sino lo cambie de estado 
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.isDelete = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

#:::
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
#:::
class DetailViewSet(ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
#:::

class OrderDetailListViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailListSerializer

#:::
class ExpenseViewSet(ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


# class BillsViewSet(ModelViewSet):
#     queryset = Bills.objects.all()
#     serializer_class = BillsSerializer