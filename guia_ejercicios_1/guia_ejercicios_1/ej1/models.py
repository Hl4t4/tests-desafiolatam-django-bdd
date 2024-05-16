from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.apellido} - {self.correo}'

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    usuario =  models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    # producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.usuario} - {self.nombre} - {self.apellido} - {self.correo}'
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.descripcion}'