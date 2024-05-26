from datetime import date
from registro_de_artistas.models import Artista, ArtistaGrupo, Grupo, Album

def crear_artista (nombre:str, apellido:str, cantante:bool, instrumento:str) -> Artista:
    artista = Artista(nombre = nombre, apellido=apellido, cantante = cantante, instrumento = instrumento)
    artista.save()
    return artista

def crear_grupo (nombre:str, fecha_creacion:date) -> Grupo:
    grupo = Grupo(nombre=nombre, fecha_creacion = fecha_creacion)
    grupo.save()
    return grupo

def relacion_artista_grupo (artista:Artista, grupo:Grupo, fecha_ingreso:date, creacion_registro:date, agregado_por:str) -> ArtistaGrupo:
    artista_grupo = ArtistaGrupo(artista_id = artista, grupo_id = grupo, fecha_ingreso = fecha_ingreso, creacion_registro = creacion_registro, agregado_por = agregado_por)
    artista_grupo.save()
    return artista_grupo

def agregar_album (titulo:str, year:int, grupo:Grupo) -> Album:
    album = Album(titulo = titulo, year = year, grupo_id = grupo)
    album.save()
    return album

def obtiene_artista (nombre:str, apellido:str) -> Artista:
    artista = Artista.objects.filter(nombre = nombre).filter(apellido = apellido).first()
    return artista

def obtiene_grupo (nombre:str) -> Grupo:
    grupo = Grupo.objects.filter(nombre=nombre).first()
    return grupo

def artista_pertenece_a_grupos (artista:Artista):
    if hasattr(artista, 'grupos'):
        return artista.grupos.all()
    else:
        return None

def artista_participa_albumes (artista:Artista) -> list:
    if hasattr(artista, 'grupos'):
        respuesta = []
        grupos = artista.grupos.all()
        for grupo in grupos:
            if not hasattr(grupo, 'albumes'):
                continue
            albumes = grupo.albumes.all()
            datos = {
                "grupo": grupo.nombre,
                "albumes": albumes
            }
            respuesta.append(datos)
        return respuesta
    else:
        return None

def grupo_albumes (grupo:Grupo) -> list:
    if not hasattr(grupo, 'albumes'):
        return None
    respuesta = []
    for album in grupo.albumes.all():
        respuesta.append(album)
    return respuesta