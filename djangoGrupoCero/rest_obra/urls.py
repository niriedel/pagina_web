from django.urls import path
from .views import lista_obras, detalle_obra
from rest_obra.viewslogin import login

urlpatterns = [
    path('lista_obras',lista_obras,name="lista_obras"),
    path('detalle_obra/<id>',detalle_obra,name="detalle_obra"),
    path('login',login,name="login"),
]