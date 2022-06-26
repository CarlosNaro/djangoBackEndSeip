
#importaciones propias 
from django.db import router
from rest_framework.routers import DefaultRouter
from Apps.apunte.viewSets import *
# create routers 
router = DefaultRouter()
router.register('client',ClientViewSet)
router.register('product',ProductViewSet)
router.register('bills', BillsViewSet)

