# from django.shortcuts import render

# # Create your views here.
# from rest_framework import status
# from rest_framework import viewSets
# from rest_framework import generics
# from rest_framework.response import Response
# from .viewSets import *
# from .routers import *
# from Apps.apunte.models import *
# from Apps.apunte.serializer import *

# #nuevas importaciones 
# # from rest_framework_simplejwt.views import TokenObtainPairView


# # class Login(TokenObtainPairView):
# #     viewSets_class = viewSets



# #from rest_framework.viewsets import ModelViewSet



# class view_sets(generics.RetrieveAPIView):
#     queryset = viewSets
#     #   viewSets = all()
   
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         viewSets_class = viewSets(queryset, many=True)
#         return Response(viewSets_class.data)

# # class ProductView(generics.RetrieveAPIView):
# #     permission_classes = (IsAuthenticated,)  
# #     queryset = Product.objects.all()

# #     def get(self, request, *args, **kwargs):
# #         queryset = self.get_queryset()
# #         serializer = ProductSerializer(queryset, many=True)
# #         return Response(serializer.data)

