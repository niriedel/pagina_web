from django.contrib import admin

from django.contrib import admin
from .models import Obra, Autor

# Register your models here.
admin.site.register(Obra)
admin.site.register(Autor)