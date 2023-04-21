#importaciones propias
from rest_framework import serializers
from Apps.users.models import *
from django.contrib.auth.hashers import make_password
#:::::
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

#::


#create your Serializer here 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # data['id'] = self.user.id
        data['username'] = self.user.username
        data['is_admin'] = self.user.is_superuser
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        response.data.update({
            #'id': data['id'],
            'username': data['username'],
            # 'email': data['email'],
            'is_admin': data['is_admin'],
        })
        return response















# #emciptación de passeord
#     def create(self, validated_data):  
#         user = User(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    # def update(self, instance, validated_data): #emciptación del passeord al ser actualizada
    #     update_user = super().update(instance, validated_data)
    #     update_user.set_password(validated_data['password'])
    #     update_user.save()
    #     return update_user