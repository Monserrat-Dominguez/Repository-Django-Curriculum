from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.shortcuts import redirect


from dates.views import PerfilDetailView

urlpatterns = [
       path('', lambda request: redirect('home')),
       path('<int:pk>/', PerfilDetailView.as_view(), name='home'), 
       path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)