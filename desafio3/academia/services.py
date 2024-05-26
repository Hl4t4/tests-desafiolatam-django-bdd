from academia.models import Estudiante, Direccion, Curso, Profesor
from datetime import date
import sys

def crear_curso (codigo:str, nombre:str, version:int,) -> Curso:
    curso = Curso(codigo = codigo, nombre = nombre, version = version)
    curso.save()
    return curso

def crear_profesor (rut:str, nombre:str, apellido:str, activo:bool, creado_por:str) -> Profesor:
    profesor = Profesor(rut = rut, nombre = nombre, apellido = apellido, activo = activo, creado_por = creado_por)
    profesor.save()
    return profesor

def crear_estudiante (rut:str, nombre:str, apellido:str, fecha_nac:date, activo:bool, creado_por:str) -> Estudiante:
    estudiante = Estudiante(rut = rut, nombre = nombre, apellido = apellido, fecha_nac = fecha_nac, activo = activo, creado_por = creado_por)
    estudiante.save()
    return estudiante

def crear_direccion (calle:str, numero:str, dpto:str, comuna:str, ciudad:str, region:str, estudiante:Estudiante) -> Direccion:
    direccion = Direccion(calle = calle, numero = numero, dpto = dpto, comuna = comuna, ciudad = ciudad, region = region, estudiante_id = estudiante)
    direccion.save()
    return direccion

def obtiene_estudiante (rut:str) -> Estudiante:
    return Estudiante.objects.get(rut = rut)

def obtiene_profesor (rut:str) -> Profesor:
    return Profesor.objects.get(rut = rut)

def obtiene_curso (codigo:str) -> Curso:
    return Curso.objects.get(codigo = codigo)

def agrega_profesor_a_curso (profesor:Profesor, curso:Curso) -> Profesor:
    profesor.cursos.add(curso)
    return profesor

def agrega_curso_a_estudiante (curso:Curso, estudiante:Estudiante) -> Estudiante:
    estudiante.cursos.add(curso)
    return estudiante

def agrega_cursos_a_estudiante (cursos:list[Curso], estudiante:Estudiante) -> Estudiante:
    for curso in cursos:
        agrega_curso_a_estudiante(curso, estudiante)
    return estudiante

def imprime_profesor_cursos (profesor:Profesor) -> None:
    print(f'Estudiante\n{profesor}')
    if hasattr(profesor, 'cursos'):
        for curso in profesor.cursos.all():
            print(f'Curso\n{curso}')

def imprime_estudiante_cursos (estudiante:Estudiante) -> None:
    print(f'Estudiante\n{estudiante}')
    if hasattr(estudiante, 'cursos'):
        for curso in estudiante.cursos.all():
            print(f'Curso\n{curso}')

def test() -> None: #Funcion para hacer todas las pruebas 
    estudiantes = Estudiante.objects.all()
    direcciones = Direccion.objects.all()
    cursos = Curso.objects.all()
    profesores = Profesor.objects.all()

    if estudiantes:
        estudiantes.delete()
    if direcciones:
        direcciones.delete()
    if cursos:
        cursos.delete()
    if profesores:
        profesores.delete()

    original_stdout = sys.stdout
    file = open('output.txt', 'w', encoding='utf-8')
    sys.stdout = file

    print(estudiantes)
    print(direcciones)
    print(cursos)
    print(profesores)

    print('\n')

    curso1 = crear_curso(codigo = 'abcde12345', nombre = 'nombre1', version = 5)
    curso2 = crear_curso(codigo = 'dfghh67890', nombre = 'nombre2', version = 4)
    curso3 = crear_curso(codigo = 'weiur45678', nombre = 'nombre3', version = 3)
    curso4 = crear_curso(codigo = 'oiugh90123', nombre = 'nombre4', version = 2)
    curso5 = crear_curso(codigo = 'cdbsh45678', nombre = 'nombre5', version = 1)

    print(curso1)
    print(curso2)
    print(curso3)
    print(curso4)
    print(curso5)

    print('\n')

    estudiante1 = crear_estudiante(rut = '111111111', nombre = 'nombre1', apellido = 'apellido1', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante2 = crear_estudiante(rut = '222222222', nombre = 'nombre2', apellido = 'apellido2', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante3 = crear_estudiante(rut = '333333333', nombre = 'nombre3', apellido = 'apellido3', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante4 = crear_estudiante(rut = '444444444', nombre = 'nombre4', apellido = 'apellido4', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante5 = crear_estudiante(rut = '555555555', nombre = 'nombre5', apellido = 'apellido5', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante6 = crear_estudiante(rut = '666666666', nombre = 'nombre6', apellido = 'apellido6', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante7 = crear_estudiante(rut = '777777777', nombre = 'nombre7', apellido = 'apellido7', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante8 = crear_estudiante(rut = '888888888', nombre = 'nombre8', apellido = 'apellido8', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante9 = crear_estudiante(rut = '999999999', nombre = 'nombre9', apellido = 'apellido9', fecha_nac= date.today(), activo = True, creado_por='Admin01')
    estudiante10 = crear_estudiante(rut = '000000000', nombre = 'nombre10', apellido = 'apellido10', fecha_nac= date.today(), activo = True, creado_por='Admin01')

    print(estudiante1)
    print(estudiante2)
    print(estudiante3)
    print(estudiante4)
    print(estudiante5)
    print(estudiante6)
    print(estudiante7)
    print(estudiante8)
    print(estudiante9)
    print(estudiante10)

    print('\n')

    direccion1 = crear_direccion(calle = 'calle1', numero = '1111', dpto = 'AAA', comuna = 'comuna1', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante1)
    direccion2 = crear_direccion(calle = 'calle2', numero = '2222', dpto = 'BBB', comuna = 'comuna2', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante2)
    direccion3 = crear_direccion(calle = 'calle3', numero = '3333', dpto = 'CCC', comuna = 'comuna3', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante3)
    direccion4 = crear_direccion(calle = 'calle4', numero = '4444', dpto = 'DDD', comuna = 'comuna4', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante4)
    direccion5 = crear_direccion(calle = 'calle5', numero = '5555', dpto = 'EEE', comuna = 'comuna5', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante5)
    direccion6 = crear_direccion(calle = 'calle6', numero = '6666', dpto = 'FFF', comuna = 'comuna6', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante6)
    direccion7 = crear_direccion(calle = 'calle7', numero = '7777', dpto = 'GGG', comuna = 'comuna7', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante7)
    direccion8 = crear_direccion(calle = 'calle8', numero = '8888', dpto = 'HHH', comuna = 'comuna8', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante8)
    direccion9 = crear_direccion(calle = 'calle9', numero = '9999', dpto = 'JJJ', comuna = 'comuna9', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante9)
    direccion10 = crear_direccion(calle = 'calle10', numero = '0000', dpto = 'KKK', comuna = 'comuna10', ciudad = 'Santiago', region = 'Metropolitana', estudiante = estudiante10)

    print(direccion1)
    print(direccion2)
    print(direccion3)
    print(direccion4)
    print(direccion5)
    print(direccion6)
    print(direccion7)
    print(direccion8)
    print(direccion9)
    print(direccion10)

    print('\n')

    profesor1 = crear_profesor(rut = '111111111', nombre = 'nombre1', apellido = 'apellido1', activo = True, creado_por='Admin01')
    profesor2 = crear_profesor(rut = '222222222', nombre = 'nombre2', apellido = 'apellido2', activo = True, creado_por='Admin01')
    profesor3 = crear_profesor(rut = '333333333', nombre = 'nombre3', apellido = 'apellido3', activo = True, creado_por='Admin01')
    profesor4 = crear_profesor(rut = '444444444', nombre = 'nombre4', apellido = 'apellido4', activo = True, creado_por='Admin01')
    profesor5 = crear_profesor(rut = '555555555', nombre = 'nombre5', apellido = 'apellido5', activo = True, creado_por='Admin01')
    profesor6 = crear_profesor(rut = '666666666', nombre = 'nombre6', apellido = 'apellido6', activo = True, creado_por='Admin01')
    profesor7 = crear_profesor(rut = '777777777', nombre = 'nombre7', apellido = 'apellido7', activo = True, creado_por='Admin01')
    profesor8 = crear_profesor(rut = '888888888', nombre = 'nombre8', apellido = 'apellido8', activo = True, creado_por='Admin01')
    profesor9 = crear_profesor(rut = '999999999', nombre = 'nombre9', apellido = 'apellido9', activo = True, creado_por='Admin01')
    profesor10 = crear_profesor(rut = '000000000', nombre = 'nombre10', apellido = 'apellido10', activo = True, creado_por='Admin01')

    print(profesor1)
    print(profesor2)
    print(profesor3)
    print(profesor4)
    print(profesor5)
    print(profesor6)
    print(profesor7)
    print(profesor8)
    print(profesor9)
    print(profesor10)

    print('\n')

    estudiantex = obtiene_estudiante(rut = '444444444')
    cursox = obtiene_curso(codigo = 'dfghh67890')
    profesorx = obtiene_profesor(rut = '666666666')

    print(estudiantex)
    print(cursox)
    print(profesorx)

    print('\n')

    profesory = profesor1
    profesory = agrega_profesor_a_curso(profesory, curso1)
    profesory = agrega_profesor_a_curso(profesory, curso2)
    profesory = agrega_profesor_a_curso(profesory, curso3)

    imprime_profesor_cursos(profesory)

    profesorz = profesor7
    profesorz = agrega_profesor_a_curso(profesorz, curso4)
    profesorz = agrega_profesor_a_curso(profesorz, curso5)

    imprime_profesor_cursos(profesorz)

    print('\n')

    estudiantex = estudiante4
    estudiantex = agrega_cursos_a_estudiante([curso2, curso3, curso5], estudiantex)

    imprime_estudiante_cursos(estudiantex)

    estudiantey = estudiante10
    estudiantey = agrega_cursos_a_estudiante([curso2, curso1, curso4, curso3, curso5], estudiantey)

    imprime_estudiante_cursos(estudiantey)

    print('\n')

    sys.stdout = original_stdout
    file.close()


###### Funciones a correr en shell
#from academia.services import test
#test()