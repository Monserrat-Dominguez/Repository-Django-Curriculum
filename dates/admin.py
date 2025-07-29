from django.contrib import admin
from .models import Perfil,experiencia,Historial,FormacionComplementaria

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display=('nombre','email','telefono','ubicacion','resumen','imagen')
    
@admin.register(experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'puesto', 'empresa', 'inicio', 'fin')

@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display=('categoria','titulo','institucion','ubicacion','inicio','fin','descripcion')

admin.site.register(FormacionComplementaria)
class FormacionComplementariaAdmin(admin.ModelAdmin):
    list_display=('curso','enlace')
  