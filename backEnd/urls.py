from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from ..Apps.users.urls import password_reset, password_reset_confirm
from django.contrib import admin
from django.urls import path, include

from Apps.users.serializer import CustomTokenObtainPairView  # token serializado
from Apps.users.views import Change_Password


urlpatterns = [
    path("admin/", admin.site.urls),
    # ... Otras URLs
    path("apunte/", include("Apps.apunte.urls")),
    path("users/", include("Apps.users.urls")),
    path("auth/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("change-password/", Change_Password, name="change-password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
