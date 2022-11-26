#importaciones propias
from dataclasses import fields
from imp import source_from_cache
from pyexpat import model
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


# class OrderSerializer(serializers.ModelSerializer):
#     #podemos usar otros serializadores dentro de otro serializador 
#     #metodo 1
#     # id_client = ClientSerializer()
#     #metodo 2 : usamos la clase meta(str) que se retorna en los modelos
#     # id_client = serializers.StringRelatedField()
#     # :::::::::::::::::::::::::::::::::   
#     class Meta:
#         model = Order
#         fields = '__all__'
    
#     # Metodo 3
#     # def to_representation(self, instance):
#     #     return {
#     #         'id': instance.id,
#     #         'date': instance.date,
#     #         'id_client': instance.id_client.name 
#     #     }


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'id_client': instance.id_client.name,
            'subTotal' : instance.subTotal if instance.subTotal == 'null' else '0' , 
            'total' : instance.total if instance.total == 'null' else '0',
            'date': instance.date

        }



class DetailSerializer(serializers.ModelSerializer):

    # id_product = serializers.StringRelatedField()
    # id_order = OrderSerializer()
    class Meta:
        model = Detail
        fields = '__all__' 
        # fields = ['id','id_product','amount','price']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'id_product': instance.id_product.name, 
            'amount': instance.amount,
            'price': instance.price 
        }




class OrderDetailListSerializer(serializers.ModelSerializer):
    order_details = DetailSerializer(many=True)
    id_client = serializers.StringRelatedField()
    class Meta: 
        model = Order
        fields = ['id','id_client','date','order_details']
    








class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__' 

# class BillsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bills
#         fields = '__all__'

        