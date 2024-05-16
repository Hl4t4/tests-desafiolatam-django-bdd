from desafioadl.models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas ():
    tareas = Tarea.objects.all()
    tareas_con_subtareas = [[tarea, tarea.subtarea_set.all()] for tarea in tareas]
    # subtareas = [tarea.subtarea_set.all() for tarea in tareas]
    return tareas_con_subtareas

def crear_nueva_tarea (descripcion, eliminada):
    tarea = Tarea(descripcion = descripcion, eliminada = eliminada)
    tarea.save()
    return recupera_tareas_y_sub_tareas ()

def crear_sub_tarea (descripcion, eliminada, tarea):
    subtarea = SubTarea(descripcion = descripcion, eliminada = eliminada, tarea = tarea)
    subtarea.save()
    return recupera_tareas_y_sub_tareas ()

def elimina_tarea (id):
    tarea = Tarea.objects.get(id = id)
    tarea.delete()
    return recupera_tareas_y_sub_tareas ()

def elimina_sub_tarea (id):
    subtarea = SubTarea.objects.get(id = id)
    subtarea.delete()
    return recupera_tareas_y_sub_tareas ()

def imprimir_en_pantalla (tareas_con_subtareas):
    [print(f'{tarea[0]}\n{"\n".join(str(printable) for printable in [subtarea for subtarea in tarea[1]])}\n') for tarea in tareas_con_subtareas]

#  import desafioadl.services as services  
# para script de pruebas, ver scripts.py