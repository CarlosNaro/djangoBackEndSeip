#importaciones Propias 
from Apps.users.routers import *
from django.urls import path, include
from Apps.users.viewSets import *



# Create your urls here.
urlpatterns=[

    path('',include(router.urls)),

]