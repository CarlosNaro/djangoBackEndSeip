#importaciones Propias 
from Apps.apunte.routers import *
from django.urls import path, include
from Apps.apunte.viewSets import *

# Create your urls here.
urlpatterns=[
    path('',include(router.urls)),
]