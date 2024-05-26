from datetime import date
from registro_conductores.models import Conductor, Vehiculo, Direccion

def crear_conductor(rut:str, nombre:str, apellido:str, fecha_nac:date) -> Conductor:
    print (Conductor.objects.all().__dict__)
    conductor = Conductor(rut = rut, nombre = nombre, apellido = apellido, fecha_nac = fecha_nac)
    conductor.save()
    print (Conductor.objects.all().__dict__)
    return conductor

def agregar_direccion_a_conductor(calle:str, numero:str, dpto:str, comuna:str, ciudad:str, region:str, conductor:Conductor) -> Direccion:
    print (Direccion.objects.all().__dict__)
    direccion = Direccion(calle = calle, numero = numero, dpto = dpto, comuna = comuna, ciudad = ciudad, region = region, conductor_id = conductor)
    direccion.save()
    print (Direccion.objects.all().__dict__)
    return direccion

def agregar_un_vehiculo(patente:str, marca:str, modelo:str, year:date, conductor:Conductor) -> Vehiculo:
    print (Vehiculo.objects.all().__dict__)
    vehiculo = Vehiculo(patente = patente, marca = marca, modelo = modelo, year = year, conductor_id = conductor)
    vehiculo.save()
    print (Vehiculo.objects.all().__dict__)
    return vehiculo

def eliminar_vehiculo_id(id:int):
    print (Vehiculo.objects.all().__dict__)
    Vehiculo.objects.get(id = id).delete()
    print (Vehiculo.objects.all().__dict__)

def eliminar_vehiculo(vehiculo:Vehiculo):
    print (Vehiculo.objects.all().__dict__)
    vehiculo.delete()
    print (Vehiculo.objects.all().__dict__)

def eliminar_conductor_id(id:int):
    print (Conductor.objects.all().__dict__)
    print (Vehiculo.objects.all().__dict__)
    print (Direccion.objects.all().__dict__)
    Conductor.objects.get(id = id).delete()
    print (Conductor.objects.all().__dict__)
    print (Vehiculo.objects.all().__dict__)
    print (Direccion.objects.all().__dict__)

    
def eliminar_conductor(conductor:Conductor):
    print (Conductor.objects.all().__dict__)
    print (Vehiculo.objects.all().__dict__)
    print (Direccion.objects.all().__dict__)
    conductor.delete()
    print (Conductor.objects.all().__dict__)
    print (Vehiculo.objects.all().__dict__)
    print (Direccion.objects.all().__dict__)

def test():
    print('Creacion conductor 1')
    conductor1 = crear_conductor('999999999', 'nombre1', 'apellido1', date(year=2000, month=1, day=1))
    print('Creacion conductor 2')
    conductor2 = crear_conductor('999955599', 'nombre2', 'apellido2', date(year=2050, month=1, day=1))
    print('Agregar direccion 1 a conductor 1')
    direccion1 = agregar_direccion_a_conductor('calle', numero='7369', dpto='504', comuna='Florida', ciudad = 'ciudad', region= 'region', conductor= conductor1)
    print('Agregar vehiculo 1 a conductor 1')
    vehiculo1 = agregar_un_vehiculo(patente='420420', marca='Si', modelo='modelo', year = date(year=3000, month=1, day=1), conductor=conductor1)
    print('Eliminar vehiculo 1')
    eliminar_vehiculo(vehiculo1)
    print('Eliminar conductor 1')
    eliminar_conductor(conductor=conductor1)

# from registro_conductores.services import test
# test()