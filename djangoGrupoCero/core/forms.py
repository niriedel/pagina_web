from django import forms
from django.forms import ModelForm
from .models import Obra

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre','historia','descripcion','precio','tecnica','nombreAutor', 'imagen']
        