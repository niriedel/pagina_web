from django.urls import path, include
import imp
from .views import index, login, register, api, artista_dad, artista_imp, artista_med, ca_dad, ca_imp, ca_med, obra_dad, obra_med, obra_imp, buscar, usuario_carrito, usuario_estadoProducto, usuario_inicio, ver_obras, form_add_obra, form_mod_obra, form_del_obra, admin_inicio, admin_aceptarRechazarProducto,api_index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    #carpeta acceso
    path('acceso/login/', login, name="login"),
    path('acceso/register/', register, name="register"),
    #carpeta api
    path('api/', api, name="api"),
    path('api/core/index.html/', api_index, name="api_index"),
    #carpeta artistas
    path('artistas/art_dad/', artista_dad, name="art_dad"),
    path('artistas/art_imp/', artista_imp, name="art_imp"),
    path('artistas/art_med/', artista_med, name="art_med"),
    #carpeta categorias
    path('categorias/ca_dad/', ca_dad, name="ca_dad"),
    path('categorias/ca_imp/', ca_imp, name="ca_imp"),
    path('categorias/ca_med/', ca_med, name="ca_med"),
    #carpeta obras
    path('obras/obra_dad/', obra_dad, name="obra_dad"),
    path('obras/obra_imp/', obra_imp, name="obra_imp"),
    path('obras/obra_med/', obra_med, name="obra_med"),
    #carpeta buscar
    path('buscar/', buscar, name="buscar"),
    #carpeta usuario
    path('usuario/carrito/', usuario_carrito, name="usuario_carrito"),
    path('usuario/estadoProducto/', usuario_estadoProducto, name="usuario_estadoProducto"),
    path('usuario/inicio/', usuario_inicio, name="usuario_inicio"),
    #archivos form
    path('usuario/publicar/', form_add_obra, name="form_add_obra"),
    path('form-mod-obra/<id>', form_mod_obra, name="form_mod_obra"),
    path('form-del-obra/<id>', form_del_obra, name="form_del_obra"),
    #carpeta admin
    path('administrador/inicio/', admin_inicio, name="admin_inicio"),
    path('administrador/aceptarRechazarProducto/', admin_aceptarRechazarProducto, name="admin_aceptarRechazarProducto"),
    path('administrador/ver_obras/', ver_obras, name="ver_obras")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )