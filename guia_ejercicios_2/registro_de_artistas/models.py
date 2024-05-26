from django.db import models

# Create your models here.

class Artista (models.Model):
    id = models.AutoField(primary_key=True, null = False, unique = True)
    nombre = models.CharField(null = False, blank = False, max_length= 50)
    apellido = models.CharField(null = False, blank = False, max_length= 50)
    cantante = models.BooleanField(default=False)
    instrumento = models.CharField(null = True, blank = False, max_length= 50)
    grupos = models.ManyToManyField(to = "Grupo", related_name='artistas', through= 'ArtistaGrupo')

class Grupo (models.Model):
    id = models.AutoField(primary_key=True, null = False, unique = True)
    nombre = models.CharField(null = False, blank = False, max_length= 50)
    fecha_creacion = models.DateField(null = False)

class ArtistaGrupo(models.Model):
    artista_id = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True)
    grupo_id = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True)
    fecha_ingreso = models.DateField()
    creacion_registro = models.DateField()
    agregado_por = models.CharField(max_length=50) #Dice date el modelo pero probablemente este mal

class Album(models.Model):
    id = models.AutoField(primary_key=True, null = False, unique = True)
    titulo = models.CharField(null = False, blank = False, max_length= 50)
    year = models.IntegerField(null = False)
    grupo_id = models.ForeignKey(Grupo, related_name="albumes", on_delete=models.CASCADE, null=False)
