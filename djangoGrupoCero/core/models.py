from distutils.command.upload import upload
from django.db import models

# Create your models here.

# Modelo para obra
# class Autor(models.Model):
#   idAutor = models.IntegerField(primary_key = True, verbose_name = 'Id del autor')
#   nombreAutor = models.CharField(max_length = 60, verbose_name = 'Nombre del autor')
#   apellidoAutor = models.CharField(max_length = 60, verbose_name = 'Apellido del autor')

#   def __str__(self):
#     return self.nombreAutor

class Obra(models.Model):
  nombre = models.CharField (max_length = 60, verbose_name = 'Nombre')
  imagen = models.ImageField(verbose_name = 'Imagen', upload_to="obrasimg", null=True)
  historia = models.CharField(max_length = 250, verbose_name = 'Historia')
  descripcion = models.CharField(max_length = 250, verbose_name = 'Descripcion')
  precio = models.IntegerField(verbose_name = 'Precio')
  tecnica = models.CharField(max_length = 75, verbose_name = 'Tecnica usada')
  nombreAutor = models.CharField(max_length = 75, verbose_name = 'Nombre autor')
  # idAutor = models.ForeignKey(Autor, on_delete = models.CASCADE)

  def __str__(self):
    return self.nombre

class Usuario(models.Model):
  nombre = models.CharField (max_length = 24, verbose_name = 'Nombre')
  apellido = models.CharField(max_length = 24, verbose_name = 'Apellido')
  email = models.EmailField(max_length = 60, verbose_name = 'Email')
  contraseña = models.CharField(max_length = 24, verbose_name = 'Contraseña')

  def __str__(self):
    return self.nombre
    

  

  



