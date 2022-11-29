from django.contrib import admin

# Register your models here.

from vendor.models import vendor_model
admin.site.register(vendor_model)