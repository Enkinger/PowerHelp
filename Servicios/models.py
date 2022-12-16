from django.db import models

# Create your models here.
opciones_clientes = [
    ['No Profesional','No Profesional'],
    ['Profesional','Profesional'],
    ['Empresa','Empresa'],
    ['ONG`S','ONG`S'],
    
]

class Post(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo = models.CharField( max_length=50,choices=opciones_clientes)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
