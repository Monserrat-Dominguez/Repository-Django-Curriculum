from django.http import HttpResponse
from django.views.generic import DetailView
from .models import FormacionComplementaria, Historial, Perfil, experiencia

# 19546

class PerfilDetailView(DetailView):
    model = Perfil
    template_name = 'dates/index.html'  
    context_object_name = 'perfil'
