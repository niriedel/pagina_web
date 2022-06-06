from django.shortcuts import render
from .models import Obra
from .forms import ObraForm
# Create your views here.

def form_mod_obra(request, id):
    obra = Obra.objects.get(idObra=id)
    datos = {
        'form': ObraForm(instance=obra)
    }
    
    return render(request, 'core/form_mod_obra.html', datos)

def form_obra(request):
    contexto = { 
        'form': ObraForm(),
        }
    if request.method=='POST':
        formulario=ObraForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos guardados correctamente'
    return render(request, 'core/form_obra.html', contexto)

def tabla(request):
    listaObras = Obra.objects.all()
    contexto = {
        'obras': listaObras,
    }
    return render(request, 'core/tabla/index.html', contexto)

def index(request):
    return render(request, 'core/index.html')

#carpeta acceso
def login(request):
    return render(request, 'core/acceso/login/index.html')

def register(request):
    return render(request, 'core/acceso/register/index.html')

#carpeta aceptarRechazarProducto
def aceptarRechazarProducto(request):
    return render(request, 'core/aceptarRechazarProducto/index.html')

#carpeta api
def api(request):
    return render(request, 'core/api/index.html')

#carpeta artistas
def artista_dad(request):
    return render(request, 'core/artistas/art_dad/index.html')

def artista_imp(request):
    return render(request, 'core/artistas/art_imp/index.html')

def artista_med(request):
    return render(request, 'core/artistas/art_med/index.html')

#carpeta buscar
def buscar(request):
    return render(request, 'core/buscar/index.html')

#carpeta categorias
def ca_dad(request):
    return render(request, 'core/categorias/ca_dad/index.html')

def ca_imp(request):
    return render(request, 'core/categorias/ca_imp/index.html')

def ca_med(request):
    return render(request, 'core/categorias/ca_med/index.html')

#carpeta obras
def obra_dad(request):
    return render(request, 'core/obras/obra_dad/index.html')

def obra_imp(request):
    return render(request, 'core/obras/obra_imp/index.html')

def obra_med(request):
    return render(request, 'core/obras/obra_med/index.html')

#carpeta usuario
def usuario_carrito(request):
    return render(request, 'core/usuario/carrito/index.html')

def usuario_estadoProducto(request):
    return render(request, 'core/usuario/estadoProducto/index.html')

def usuario_inicio(request):
    return render(request, 'core/usuario/inicio/index.html')

def usuario_publicar(request):
    return render(request, 'core/usuario/publicar/index.html')
