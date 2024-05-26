from registro_contabilidad.models import Chofer, Vehiculo, RegistroContabilidad
from datetime import date
import sys

def crear_vehiculo (patente:str, marca:str, modelo:str, year:int, activo:bool) -> Vehiculo:
    vehiculo = Vehiculo(patente = patente, marca = marca, modelo = modelo, year = year, activo = activo)
    vehiculo.save()
    return vehiculo

def crear_chofer (rut:str, nombre:str, apellido:str, activo:bool, creacion_registro:date, vehiculo:Vehiculo) -> Chofer:
    chofer = Chofer(rut = rut, nombre = nombre, apellido = apellido, activo = activo, creacion_registro = creacion_registro, vehiculo_id = vehiculo)
    chofer.save()
    return chofer

def crear_registro_contable (fecha_compra:date, valor:float, vehiculo:Vehiculo):
    if vehiculo != None:
        registro_contable = RegistroContabilidad(fecha_compra = fecha_compra, valor = valor, vehiculo_id = vehiculo)
        registro_contable.save()
        return registro_contable
    else:
        return None

def deshabilitar_chofer (chofer:Chofer) -> Chofer:
    chofer.activo = False
    chofer.save()
    return chofer

def deshabilitar_vehiculo (vehiculo:Vehiculo) -> Vehiculo:
    vehiculo.activo = False
    vehiculo.save()
    return vehiculo

def habilitar_chofer (chofer:Chofer) -> Chofer:
    chofer.activo = True
    chofer.save()
    return chofer

def habilitar_vehiculo (vehiculo:Vehiculo) -> Vehiculo:
    vehiculo.activo = True
    vehiculo.save()
    return vehiculo

def obtener_vehiculo (patente:str) -> Vehiculo:
    return Vehiculo.objects.get(patente = patente)

def obtener_chofer (rut:str) -> Chofer:
    return Chofer.objects.get(rut = rut)

def asignar_chofer_a_vehiculo (chofer:Chofer, vehiculo:Vehiculo) -> Chofer:
    chofer.vehiculo_id = vehiculo
    chofer.save()
    return chofer

def imprimir_datos_vehiculos () -> None:
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        chofer = ''
        registro_contabilidad = ''
        if hasattr(vehiculo, 'chofer'):
            chofer = vehiculo.chofer
        if hasattr(vehiculo, 'registro_contabilidad'):
            registro_contabilidad = vehiculo.registro_contabilidad
        print(f'Chofer:\n{chofer}\nVehiculo:\n{vehiculo}\nRegistro de Contabilidad:\n{registro_contabilidad}\n')


# Funcion para probar todos los servicios
def test() -> None:
    vehiculos = Vehiculo.objects.all()
    choferes = Chofer.objects.all()
    registros = RegistroContabilidad.objects.all()

    if vehiculos:
        vehiculos.delete()
    if choferes:
        choferes.delete()
    if registros:
        registros.delete()

    original_stdout = sys.stdout
    file = open('output.txt', 'w', encoding='utf-8')
    sys.stdout = file

    print(vehiculos)
    print(choferes)
    print(registros)

    print('\n')

    vehiculo1 = crear_vehiculo(patente='abc123', marca='marca1', modelo='modelo1', year= 1990, activo= True)
    vehiculo2 = crear_vehiculo(patente='abc999', marca='marca3', modelo='modelo3', year= 1999, activo= True)
    vehiculo3 = crear_vehiculo(patente='abc666', marca='marca2', modelo='modelo2', year= 2000, activo= True)
    vehiculo4 = crear_vehiculo(patente='def123', marca='marca1', modelo='modelo1', year= 2010, activo= True)
    vehiculo5 = crear_vehiculo(patente='tgh123', marca='marca2', modelo='modelo2', year= 2020, activo= True)

    print(vehiculo1)
    print(vehiculo2)
    print(vehiculo3)
    print(vehiculo4)
    print(vehiculo5)

    print('\n')


    chofer1 = crear_chofer(rut= '111111111', nombre= 'nombre1', apellido='apellido1', activo= True, creacion_registro=date.today(), vehiculo=None)
    chofer2 = crear_chofer(rut= '222222222', nombre= 'nombre2', apellido='apellido2', activo= True, creacion_registro=date.today(), vehiculo=None)
    chofer3 = crear_chofer(rut= '333333333', nombre= 'nombre3', apellido='apellido3', activo= True, creacion_registro=date.today(), vehiculo=None)
    chofer4 = crear_chofer(rut= '444444444', nombre= 'nombre4', apellido='apellido4', activo= True, creacion_registro=date.today(), vehiculo=None)
    chofer5 = crear_chofer(rut= '555555555', nombre= 'nombre5', apellido='apellido5', activo= True, creacion_registro=date.today(), vehiculo=None)
    chofer6 = crear_chofer(rut= '666666666', nombre= 'nombre6', apellido='apellido6', activo= False, creacion_registro=date.today(), vehiculo=None)

    print(chofer1)
    print(chofer2)
    print(chofer3)
    print(chofer4)
    print(chofer5)
    print(chofer6)

    print('\n')

    chofer1 = asignar_chofer_a_vehiculo(chofer = chofer1, vehiculo = vehiculo1)
    chofer2 = asignar_chofer_a_vehiculo(chofer = chofer2, vehiculo = vehiculo2)
    chofer3 = asignar_chofer_a_vehiculo(chofer = chofer3, vehiculo = vehiculo3)
    chofer4 = asignar_chofer_a_vehiculo(chofer = chofer4, vehiculo = vehiculo4)
    chofer5 = asignar_chofer_a_vehiculo(chofer = chofer5, vehiculo = vehiculo5)

    print(chofer1)
    print(chofer2)
    print(chofer3)
    print(chofer4)
    print(chofer5)
    print(chofer6)

    print('\n')

    registro1 = crear_registro_contable(fecha_compra = date.today(), valor = 999.99, vehiculo = vehiculo1)
    registro2 = crear_registro_contable(fecha_compra = date.today(), valor = 1999.99, vehiculo = vehiculo2)
    registro3 = crear_registro_contable(fecha_compra = date.today(), valor = 2999.99, vehiculo = vehiculo3)
    registro4 = crear_registro_contable(fecha_compra = date.today(), valor = 3999.99, vehiculo = vehiculo4)
    registro5 = crear_registro_contable(fecha_compra = date.today(), valor = 4999.99, vehiculo = vehiculo5)

    print(registro1)
    print(registro2)
    print(registro3)
    print(registro4)
    print(registro5)
    
    print('\n')

    print(chofer3)
    print(chofer5)

    print('\n')

    chofer3 = deshabilitar_chofer(chofer = chofer3)
    chofer5 = deshabilitar_chofer(chofer = chofer5)

    print(chofer3)
    print(chofer5)

    print('\n')


    print(chofer6)
    chofer6 = habilitar_chofer(chofer = chofer6)
    print(chofer6)

    print('\n')

    print(vehiculo1)
    print(vehiculo4)

    print('\n')

    vehiculo1 = deshabilitar_vehiculo(vehiculo = vehiculo1)
    vehiculo4 = deshabilitar_vehiculo(vehiculo = vehiculo4)

    print(vehiculo1)
    print(vehiculo4)

    print('\n')


    choferx = obtener_chofer(rut = '666666666')
    vehiculox = obtener_vehiculo(patente = 'abc123')

    print(choferx)
    print(vehiculox)

    print('\n')

    imprimir_datos_vehiculos()

    sys.stdout = original_stdout
    file.close()
    
# from registro_contabilidad.services import test
# test()
