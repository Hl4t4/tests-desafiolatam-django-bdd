from ej1.models import Persona
from django.db import connection


p1 = Persona(nombre = "Juan", apellido = "Soto", correo = "juan.soto@gmail.com")
p2 = Persona(nombre = "Nombre", apellido = "Pila", correo = "nombre.pila@gmail.com")

p1.save()
p2.save()

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM ej1_persona")
    row = cursor.fetchall()
    for p in row:
        print(f'{p[0]} - {p[1]} - {p[2]} - {p[3]}')

## Con SQL

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM ej1_persona WHERE nombre = %s AND apellido = %s", ['Juan', 'Soto'])
    row = cursor.fetchall()
    for p in row:
        print(f'{p[0]} - {p[1]} - {p[2]} - {p[3]}')

### Con ORM

print(Persona.objects.filter(nombre = 'Juan', apellido = 'Soto').first())

with connection.cursor() as cursor:
    cursor.execute("INSERT INTO ej1_persona (nombre, apellido, correo) VALUES ('Chuck', 'Norris', 'chuck.norris@chuck.norris')")
    cursor.execute("SELECT * FROM ej1_persona")
    row = cursor.fetchall()
    for p in row:
        print(f'{p[0]} - {p[1]} - {p[2]} - {p[3]}')

#### Ejercicio 2

from ej1.models import Cliente, Producto
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("INSERT INTO ej1_cliente (usuario, nombre, apellido, correo) VALUES ('chucky', 'Chuck', 'Norris', 'chuck.norris@chuck.norris')")
    cursor.execute("SELECT * FROM ej1_cliente")
    row = cursor.fetchall()
    for p in row:
        print(f'{p[0]} - {p[1]} - {p[2]} - {p[3]} - {p[4]} - {p[5]}')

c1 = Cliente(usuario = 'chucky', nombre = 'Chuck', apellido = 'Norris', correo = 'chuck.norris@chuck.norris')
c1.save()

p1 = Producto(descripcion="producto1")
p2 = Producto(descripcion="producto2")
p1.save()
p2.save()

p1.cliente = c1
p2.cliente = c1
p1.save()
p2.save()
c1.save()

c1 = Cliente.objectsfirst()
productos = c1.producto_set.all()

print(c1)
print(productos)


Cliente.objects.all().delete()
Producto.objects.all().delete()