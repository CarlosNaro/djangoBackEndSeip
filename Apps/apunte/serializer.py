#importaciones propias
from rest_framework import serializers
from Apps.apunte.models import *

#create your Serializer here 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'

        