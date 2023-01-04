#importaciones propias 
from django.db import router
from rest_framework.routers import DefaultRouter
from Apps.users.viewSets import *

# create routers 
router = DefaultRouter()
router.register('user',UserViewSet)

