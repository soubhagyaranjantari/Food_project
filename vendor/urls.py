from django.contrib import admin
from django.urls import path
from accounts import views
app_name='vendor'
urlpatterns=[
    path('registerVendor/',views.registerVendorr,name='registerVendor')
    # path('registerVendor/',views.registerVendorr,name='registrationVendor')
]