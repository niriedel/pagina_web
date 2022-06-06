from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

#carpeta acceso
def login(request):
    return render(request, 'core/acceso/login/index.html')

def register(request):
    return render(request, 'core/acceso/register/index.html')

# def aceptarRechazarProducto aqui

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


