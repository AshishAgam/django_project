from django.urls import path
from accounts.views import loginPage, register

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('register/', register, name="register")
]
