from django import forms
from django.forms import ModelForm
from .models import Obra, Usuario

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre','historia','descripcion','precio','tecnica','nombreAutor', 'imagen']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','email','contraseña']
        