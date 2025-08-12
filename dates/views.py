from django.shortcuts import render

from django.views.generic import DetailView
from .models import FormacionComplementaria, Historial, Perfil,experiencia

class PerfilDetailView(DetailView):
    model = Perfil
    template_name = 'dates/index.html'
    context_object_name = 'perfil'

    def get_object(self, queryset=None):
        perfil = Perfil.objects.first()
        if not perfil:
            raise Http404("No se encontró ningún perfil.")
        return perfil
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historial'] = Historial.objects.all()
        context['experiencias'] = experiencia.objects.all()
        context['formacion'] = FormacionComplementaria.objects.all()
        return context
