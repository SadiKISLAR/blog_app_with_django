from django.urls import path
from .views import register, user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', register, name='user_login'),
    path('login/', register, name='user_login'),
]
