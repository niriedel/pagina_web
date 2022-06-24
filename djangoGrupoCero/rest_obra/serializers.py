from rest_framework import serializers
from core.models import Obra

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = ['nombre', 'imagen', 'historia', 'descripcion', 'precio', 'tecnica', 'nombreAutor']

