from django.contrib import admin


from accounts.models import User,userProfile

from django.contrib.auth.admin import UserAdmin

# Register your models here.

class customerUserAdmin(UserAdmin):
    filter_horizontal=()
    list_filter =()
    fieldsets=()
    list_display=('username','first_name', 'last_name','role','email','is_staff','password')
    
admin.site.register(User,customerUserAdmin)
admin.site.register(userProfile)
