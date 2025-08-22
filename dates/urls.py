from django.urls import path
from django.shortcuts import redirect
from .views import PerfilDetailView

def home_redirect(request):
    return redirect('home', pk=1)  

urlpatterns = [
    path('', home_redirect),  
    path('home/<int:pk>/', PerfilDetailView.as_view(),  name='home'),
]

