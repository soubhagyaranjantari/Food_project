from django.urls import path
from accounts import views

app_name='accounts'
urlpatterns=[
    path('registrationUser/',views.registrationUser,name='registrationUser'),
    path('login/',views.user_login,name='login'),
    path('user_dashboard/',views.dashboard,name='user_dashboard'),
    path('cus_dashboard/',views.dashboard2,name='cus_dashboard'),
    path('logout/',views.user_logout,name='logout'),
]

#'http://127.0.0.1:8000/accounts/registerUser/' This is the register user from 


# from django.contrib.auth import views as auth_views
    # path('loginUser/',auth_views.LoginView.as_view(),name='loginUser')
    # path('login', auth_views.LoginView.as_view(), name='login'),