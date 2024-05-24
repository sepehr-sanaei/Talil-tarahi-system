from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MyAccountView.as_view(), name='account_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('login/', MyLoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

