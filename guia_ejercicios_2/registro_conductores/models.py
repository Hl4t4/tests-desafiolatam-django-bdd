from django.db import models

# Create your models here.

class Conductor (models.Model):
    rut = models.CharField(primary_key=True, null = False, unique = True, max_length= 9)
    nombre = models.CharField(null = False, blank = False, max_length= 50)
    apellido = models.CharField(null = False, blank = False, max_length= 50)
    fecha_nac = models.DateField(null = False, auto_now=False, auto_now_add=False)

class Vehiculo (models.Model):
    id = models.AutoField(primary_key=True, null = False, unique = True)
    patente = models.CharField(null = False, unique = True, max_length=6)
    marca = models.CharField(null = False, max_length=50)
    modelo = models.CharField(null = False, max_length=50)
    year = models.DateField(null = False)
    conductor_id = models.ForeignKey(Conductor, on_delete=models.CASCADE)

class Direccion (models.Model):
    id = models.AutoField(primary_key=True, null = False, unique = True)
    calle = models.CharField(null = False, max_length=50)
    numero = models.CharField(null = False, max_length=10)
    dpto = models.CharField(null = False, max_length=10)
    comuna = models.CharField(null = False, max_length=50)
    ciudad = models.CharField(null = False, max_length=50)
    region = models.CharField(null = False, max_length=50)
    conductor_id = models.OneToOneField(Conductor, on_delete=models.CASCADE)




