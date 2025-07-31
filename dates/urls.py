
from django.urls import path
from dates.views import PerfilDetailView

urlpatterns = [
    path('', PerfilDetailView.as_view(), kwargs={'pk': 1}, name='index'),
]