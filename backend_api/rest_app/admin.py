from django.contrib import admin

# Register your models here.
from .models import Product,PaymentHistory




admin.site.register(Product)
admin.site.register(PaymentHistory)