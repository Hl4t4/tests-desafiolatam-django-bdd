from django.db import models

# Create your models here.

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    cliente_activo = models.BooleanField(default=True)

