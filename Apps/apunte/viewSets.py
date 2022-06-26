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
class BillsViewSet(ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer