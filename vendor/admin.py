from django.contrib import admin
from django.db import models
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from vendor.models import vendor_model
from accounts.models import User
class VendorUserAdmin(admin.ModelAdmin):
    filter_horizontal=()
    list_filter =()
    fieldsets=()
    list_display=("vendor_name","is_approved",'user','vendor_license',)
admin.site.register(vendor_model,VendorUserAdmin)
# admin.site.register(VendorUserAdmin)