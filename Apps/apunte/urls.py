# importaciones Propias
from Apps.apunte.routers import *
from django.urls import path, include
from Apps.apunte.viewSets import *

# from django.conf import settings
# from django.conf.urls.static import static


# Create your urls here.
urlpatterns = [
    path("", include(router.urls)),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
