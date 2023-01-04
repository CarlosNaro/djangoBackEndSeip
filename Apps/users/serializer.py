#importaciones propias

from rest_framework import serializers
from Apps.users.models import *

#create your Serializer here 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
