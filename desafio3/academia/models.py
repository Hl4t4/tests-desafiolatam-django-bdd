from django.db import models

# Create your models here.

class Estudiante (models.Model):
    rut = models.CharField(primary_key =True, null = False, unique = True, max_length = 9)
    nombre = models.CharField(null = False, blank = False, max_length = 50)
    apellido = models.CharField(null = False, blank = False, max_length = 50)
    fecha_nac = models.DateField(null = False)
    activo = models.BooleanField(default = False)
    creacion_registro = models.DateField(auto_now_add = True)
    modificacion_registro = models.DateField(auto_now = True)
    creado_por = models.CharField(max_length = 50)
    cursos = models.ManyToManyField(to = "Curso", related_name='estudiantes', null= True)

    def __str__(self):
        return f'RUT: {self.rut}\n Nombre: {self.nombre}\n Apellido: {self.apellido}\n Fecha de Nacimiento: {self.fecha_nac}\n Activo: {self.activo}\n Creacion Registro: {self.creacion_registro}\n Modificacion_Registro = {self.modificacion_registro}\n Creador por: {self.creado_por}'

class Direccion (models.Model):
    id = models.AutoField(primary_key = True, null = False, unique = True)
    calle = models.CharField(null = False, blank = False, max_length = 50)
    numero = models.CharField(null = False, blank = False, max_length = 10)
    dpto = models.CharField(null = True, blank = False, max_length = 10)
    comuna = models.CharField(null = False, blank = False, max_length = 50)
    ciudad = models.CharField(null = False, blank = False, max_length = 50)
    region = models.CharField(null = False, blank = False, max_length = 50)
    estudiante_id = models.OneToOneField(Estudiante, on_delete=models.CASCADE, unique = True, null = False)

    def __str__(self):
        return f'ID: {self.id}\n Calle: {self.calle} {self.numero}, {self.dpto}, {self.comuna}, {self.region}'

class Curso(models.Model):
    codigo = models.CharField(primary_key =True, null = False, unique = True, max_length = 10)
    nombre = models.CharField(null = False, blank = False, max_length = 50)
    version = models.IntegerField(null = True)
    
    def __str__(self):
        return f'Codigo: {self.codigo}\n Nombre: {self.nombre}\n Version: {self.version}'
    # profesor_id = models.ManyToManyField(to = "Profesor", related_name='cursos', unique=True) 

class Profesor(models.Model):
    rut = models.CharField(primary_key =True, null = False, unique = True, max_length = 9)
    nombre = models.CharField(null = False, blank = False, max_length = 50)
    apellido = models.CharField(null = False, blank = False, max_length = 50)
    activo = models.BooleanField(default = False)
    creacion_registro = models.DateField(auto_now_add = True)
    modificacion_registro = models.DateField(auto_now = True)
    creado_por = models.CharField(max_length = 50)
    cursos = models.ManyToManyField(to = "Curso", related_name='profesores', null= True)
    
    def __str__(self):
        return f'RUT: {self.rut}\n Nombre: {self.nombre}\n Apellido: {self.apellido}\n Creacion Registro: {self.creacion_registro}\n Modificacion_Registro = {self.modificacion_registro}\n Creador por: {self.creado_por}'
