"""backEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from ..Apps.users.urls import password_reset, password_reset_confirm
from django.contrib import admin
from django.urls import path, include


from Apps.users.serializer import CustomTokenObtainPairView   # token serializado



urlpatterns = [
    path('admin/', admin.site.urls),
    # ***** djoser 
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # ***** djoser 

    path('apunte/', include('Apps.apunte.urls')),
    path('users/', include('Apps.users.urls')),
    
    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
