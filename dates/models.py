from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=100) 
    email = models.EmailField()
    telefono = models.CharField(max_length=20, default='+52 000-000-0000')
    ubicacion = models.CharField(max_length=100)
    resumen = models.TextField(max_length=800)
    imagen = models.ImageField(upload_to='perfiles', blank=True, null=True)

    def __str__(self): return self.nombre

class Historial(models.Model):
    categoria = models.CharField(max_length=50)  
    titulo = models.CharField(max_length=100)    
    institucion = models.CharField(max_length=100) 
    ubicacion = models.CharField(max_length=100, blank=True)
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.categoria}: {self.titulo} en {self.institucion}"
  
class experiencia(models.Model):
    perfil=models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='experiencia')
    puesto=models.CharField(max_length=120)
    empresa=models.CharField(max_length=120)
    description=models.TextField()
    inicio=models.DateField(null=True,blank=True)
    fin=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.puesto} en {self.empresa}"
    
    
class FormacionComplementaria(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='formacion')
    curso=models.CharField(max_length=100)
    enlace = models.URLField(blank=True)
    
    def __str__(self):
        return self.curso