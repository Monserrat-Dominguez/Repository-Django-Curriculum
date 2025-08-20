from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView

from .models import FormacionComplementaria, Historial, Perfil, experiencia


class PerfilDetailView(DetailView):
    model = Perfil
    template_name = 'dates/index.html'  
    context_object_name = 'perfil'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historial'] = Historial.objects.all()
        context['experiencias'] = experiencia.objects.all()
        context['formacion'] = FormacionComplementaria.objects.all()
        return context
