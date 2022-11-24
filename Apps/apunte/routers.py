
#importaciones propias 
from django.db import router
from rest_framework.routers import DefaultRouter
from Apps.apunte.viewSets import *
# create routers 
router = DefaultRouter()
router.register('client',ClientViewSet)
router.register('product',ProductViewSet)
router.register('order', OrderViewSet)
router.register('detail', DetailViewSet)
router.register('expense', ExpenseViewSet)
router.register('orderDetails',OrderDetailListViewSet)
#router.register('bills', BillsViewSet)

