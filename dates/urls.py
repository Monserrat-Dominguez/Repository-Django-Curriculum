
from django.urls import path
from .views import PerfilDetailView

urlpatterns = [
    path('perfil/<int:pk>/', PerfilDetailView.as_view(), name='perfil-detail'),
]