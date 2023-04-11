#importaciones propias

from rest_framework import serializers
from Apps.users.models import *


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


