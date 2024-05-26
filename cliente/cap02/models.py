from django.db import models

# Create your models here.

class Cliente (models.Model):
    cliente_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    apellido = models.CharField(max_length = 50, null = False, blank = False)
    edad = models.IntegerField(blank = True, null = True)
    creacion = models.DateTimeField(auto_now_add = True)
    creacion = models.DateTimeField(auto_now = True)

class Direccion (models.Model):
    id = models.AutoField(primary_key = True)
    calle = models.CharField(max_length = 100, null = False, blank = False)
    numero = models.CharField(max_length = 10, null = False, blank = False)
    dpto = models.CharField(max_length = 10, null = True, blank = False)
    comuna = models.CharField(max_length = 10, null = False, blank = False)
    ciudad = models.CharField(max_length = 10, null = False, blank = False)
    cliente_id = models.OneToOneField(Cliente, blank = False, null = False, on_delete=models.CASCADE)

class Libro(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)

class Autor(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    libros = models.ManyToManyField(Libro, related_name="autores", through="AutorLibro")
    # libros = models.ManyToManyField(Libro, related_name="autores", through=_("AutorLibro"))

class AutorLibro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    creado_por = models.CharField(max_length=50, null=False, blank=False)
    creacion = models.DateTimeField(auto_now_add=True)

#     from cap02.models import Autor, Libro, AutorLibro
# autor1 = Autor(nombre="Joe", apellido="Rogan")
# autor1.save()
# autor2 = Autor(nombre="David", apellido="Blaine")
# autor2.save()
# autor3 = Autor(nombre="Lex", apellido="Fridman")
# autor3.save()
# autor4 = Autor(nombre="Jack", apellido="Dorsey")
# autor4.save()

# libro1 = Libro(titulo="Libro entretenido cap1", year=2020)
# libro1.save()
# libro2 = Libro(titulo="Libro entretenido cap2", year=2021)
# libro2.save()

# libro1.autores.add(autor1)
# libro1.autores.add(autor3)

# relacion1 = AutorLibro.objects.filter(autor=autor1).filter(libro=libro1).first()
# print(relacion1.creado_por)

# print(relacion1.creacion)
# relacion1.creado_por="Admin01"
# relacion1.save()
# print(relacion1.creado_por)

# relacion2 = AutorLibro.objects.filter(autor=autor3).filter(libro=libro1).first()
# print(relacion2.creado_por)
# relacion2.creado_por="Admin01"
# relacion2.save()
# print(relacion2.creado_por)
# print(relacion2.creacion)

# relacion1_l2 = AutorLibro(autor=autor2, libro=libro2, creado_por="Admin02")
# relacion1_l2.save()

# libro2.autores.all()
# relacion2_l2 = AutorLibro(autor=autor4, libro=libro2, creado_por="Admin02")
# relacion2_l2.save()

# libro2.autores.all()