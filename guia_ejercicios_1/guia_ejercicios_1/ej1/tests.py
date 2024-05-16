from django.test import TestCase
from .models import Persona


# Create your tests here.

class PersonaTestCase(TestCase):
    def setUp(self):
        p1 = Persona(nombre = "Juan", apellido = "Soto", correo = "juan.soto@gmail.com")
        p2 = Persona(nombre = "Nombre", apellido = "Pila", correo = "nombre.pila@gmail.com")
        p1.save()
        p2.save()