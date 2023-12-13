from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_evento = models.CharField(max_length=200, null=True)
    creado = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    realizado = models.DateTimeField(null=True,blank=True)
    
    
    
    
    
    def __str__(self):
        return self.nombre +' ' + self.apellido 
    