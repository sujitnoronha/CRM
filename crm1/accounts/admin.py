from django.contrib import admin
from .models import *

admin.site.register(Customers)

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Tags)