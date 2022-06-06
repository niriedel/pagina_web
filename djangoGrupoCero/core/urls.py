from django.urls import path
from .views import index, login, register

urlpatterns = [
    path('', index, name="index"),
    path('acceso/login/', login, name="login"),
    path('acceso/register/', register, name="register"),

]