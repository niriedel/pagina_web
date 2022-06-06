from django.db import models

# Create your models here.

# Modelo para obra
class Autor(models.Model):
  idAutor = models.IntegerField(primary_key = True, verbose_name = 'Id del autor')
  nombreAutor = models.CharField(max_length = 60, verbose_name = 'Nombre del autor')
  apellidoAutor = models.CharField(max_length = 60, verbose_name = 'Apellido del autor')
  numObras = models.IntegerField( verbose_name = 'Numero de obras')

  def __str__(self):
    return self.nombreAutor

class Obra(models.Model):
  idObra = models.IntegerField (primary_key = True, verbose_name = 'Id de obra')
  nombre = models.CharField (max_length = 60, verbose_name = 'Nombre')
  historia = models.CharField(max_length = 250, verbose_name = 'Historia')
  descripcion = models.CharField(max_length = 250, verbose_name = 'Descripcion')
  precio = models.IntegerField(verbose_name = 'Precio')
  tecnica = models.CharField(max_length = 75, verbose_name = 'Tecnica usada')
  idAutor = models.ForeignKey(Autor, on_delete = models.CASCADE)

  def __str__(self):
    return self.nombre


