from django.shortcuts import render, redirect
from .models import Obra, Usuario
from .forms import ObraForm, UsuarioForm
# Create your views here.

def form_del_obra(request, id):
    obra = Obra.objects.get(id=id)
    obra.delete()
    return redirect(to="../administrador/ver_obras")

def form_mod_obra(request, id):
    obra = Obra.objects.get(id=id)

    datos = {
        'form': ObraForm(instance=obra)
    }

    if request.method=='POST':
        formulario=ObraForm(data=request.POST, instance=obra, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Modificado correctamente'
        datos['form'] = ObraForm(instance=Obra.objects.get(id=id))
    
    return render(request, 'core/administrador/mod_obra/form_mod_obra.html', datos)

def form_add_obra(request):
    contexto = { 
        'form': ObraForm(),
        }
    if request.method=='POST':
        formulario=ObraForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos enviados correctamente! Su obra será publicada sólo si es aprobada por el Administrador'
    return render(request, 'core/usuario/publicar/form_add_obra.html', contexto)
    
def ver_obras(request):
    listaObras = Obra.objects.all()
    contexto = {
        'obras': listaObras,
    }
    return render(request, 'core/administrador/ver_obras/index.html', contexto)

def index(request):
    return render(request, 'core/index.html')

#carpeta acceso
def login(request):
    if request.method=='POST':
        currentEmail = request.POST.get('userEmail')
        currentPassword = request.POST.get('userPassword')

        for dbEmail in Usuario.objects.values_list('email', flat=True):
            if currentEmail == dbEmail:
                dbPassword = Usuario.objects.values_list('contraseña', flat=True).get(email=dbEmail)
                if currentPassword == dbPassword:
                    return render(request, 'core/usuario/inicio/index.html')
                
        # dbEmail = Usuario.objects.values_list('email', flat=True).get(email=currentEmail)
        # if dbEmail:
        #     return render(request, 'core/usuario/inicio/index.html')
        #     dbPassword = Usuario.objects.values_list('contraseña').filter(email=currentEmail)
        #     if currentPassword == '123456':
        #         return render(request, 'core/usuario/inicio/index.html')

    return render(request, 'core/acceso/login/index.html')
            
def register(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('email') and request.POST.get('contraseña'):
            usuario=Usuario()
            usuario.nombre= request.POST.get('nombre')
            usuario.apellido= request.POST.get('apellido')
            usuario.email= request.POST.get('email')
            usuario.contraseña= request.POST.get('contraseña')
            usuario.save()

    return render(request, 'core/acceso/register/index.html')

#carpeta api
def api(request):
    return render(request, 'core/api/index.html')

def api_index(request):
    return render(request, 'api/core/index.html')

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

#carpeta administrador
def admin_inicio(request):
    return render(request, 'core/administrador/inicio/index.html')

def admin_aceptarRechazarProducto(request):
    return render(request, 'core/administrador/aceptarRechazarProducto/index.html')