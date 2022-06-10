from django import forms
from django.forms import ModelForm
from .models import Obra

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['idObra','nombre','historia','descripcion','precio','tecnica','idAutor', 'imagen']
        