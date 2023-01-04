# imprtaciones propias 
from Apps.users.models import *
from Apps.users.serializer import *
from rest_framework.viewsets import ModelViewSet
# create your ViewSets here



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#:::
