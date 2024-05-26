from django.db import models

# Create your models here.

class Chofer (models.Model):
    rut = models.CharField(primary_key=True, null = False, unique = True, max_length=9)
    nombre = models.CharField(null = False, blank = False, max_length= 50)
    apellido = models.CharField(null = False, blank = False, max_length= 50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(null = True)
    vehiculo_id = models.OneToOneField(to = "Vehiculo", on_delete=models.CASCADE, related_name='chofer' , unique = True, null = True)

    def __str__(self):
        return f'RUT: {self.rut}\n Nombre: {self.nombre}\n Apellido: {self.apellido}\n Activo: {self.activo}\n Creacion Registro: {self.creacion_registro}'


class Vehiculo (models.Model):
    patente = models.CharField(primary_key=True, null = False, unique = True, max_length=6)
    marca = models.CharField(null = False, blank = False, max_length= 20)
    modelo = models.CharField(null = False, blank = False, max_length= 20)
    year = models.IntegerField(null = False)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return f'Patente: {self.patente}\n Marca: {self.marca}\n Modelo: {self.modelo}\n Año: {self.year}\n Activo: {self.activo}'

class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True, null = False, unique = True)
    fecha_compra = models.DateField(null = True)
    valor = models.FloatField(null = False)
    vehiculo_id = models.OneToOneField(to = "Vehiculo", on_delete=models.CASCADE, related_name='registro_contabilidad', unique = True, null= False)

    def __str__(self):
        return f'ID: {self.id}\n Fecha de Compra: {self.fecha_compra}\n Valor: ${self.valor}'