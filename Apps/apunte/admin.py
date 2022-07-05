from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
from django.contrib import admin
from Apps.apunte.models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Detail)
admin.site.register(Expenses)

