from desafioadl.models import Tarea, SubTarea
import desafioadl.services as services 

def clean_database():
    Tarea.objects.all().delete()
    SubTarea.objects.all().delete()

def test():
    # services.recupera_tareas_y_sub_tareas()

    services.crear_nueva_tarea(descripcion = "tarea 1", eliminada = False)
    services.crear_nueva_tarea(descripcion = "tarea 2", eliminada = False)
    services.crear_nueva_tarea(descripcion = "tarea 3", eliminada = False)
    services.crear_nueva_tarea(descripcion = "tarea 4", eliminada = False)
    services.crear_nueva_tarea(descripcion = "tarea 5", eliminada = False)

    print("Agregadas tareas 1 a 5")
    services.imprimir_en_pantalla(services.recupera_tareas_y_sub_tareas())

    tareas = Tarea.objects.all()

    print("Agregadas subtareas 1 a 15")
    services.crear_sub_tarea(descripcion = "subtarea 1", eliminada = False, tarea = tareas[0])
    services.crear_sub_tarea(descripcion = "subtarea 2", eliminada = False, tarea = tareas[0])
    services.crear_sub_tarea(descripcion = "subtarea 3", eliminada = False, tarea = tareas[0])
    services.crear_sub_tarea(descripcion = "subtarea 4", eliminada = False, tarea = tareas[0])
    services.crear_sub_tarea(descripcion = "subtarea 5", eliminada = False, tarea = tareas[1])
    services.crear_sub_tarea(descripcion = "subtarea 6", eliminada = False, tarea = tareas[1])
    services.crear_sub_tarea(descripcion = "subtarea 7", eliminada = False, tarea = tareas[1])
    services.crear_sub_tarea(descripcion = "subtarea 8", eliminada = False, tarea = tareas[2])
    services.crear_sub_tarea(descripcion = "subtarea 9", eliminada = False, tarea = tareas[3])
    services.crear_sub_tarea(descripcion = "subtarea 10", eliminada = False, tarea = tareas[3])
    services.crear_sub_tarea(descripcion = "subtarea 11", eliminada = False, tarea = tareas[3])
    services.crear_sub_tarea(descripcion = "subtarea 12", eliminada = False, tarea = tareas[3])
    services.crear_sub_tarea(descripcion = "subtarea 13", eliminada = False, tarea = tareas[3])
    services.crear_sub_tarea(descripcion = "subtarea 14", eliminada = False, tarea = tareas[4])
    services.crear_sub_tarea(descripcion = "subtarea 15", eliminada = False, tarea = tareas[4])

    services.imprimir_en_pantalla(services.recupera_tareas_y_sub_tareas())

    print("Eliminada tareas 3")
    services.elimina_tarea(tareas[2].id)

    services.imprimir_en_pantalla(services.recupera_tareas_y_sub_tareas())

    print("Eliminada subtarea 14")
    services.elimina_sub_tarea(tareas[3].subtarea_set.first().id)

    services.imprimir_en_pantalla(services.recupera_tareas_y_sub_tareas())

 # python manage.py sqlsequencereset desafioadl
 # import desafioadl.scripts as script
 # script.clean_database()
 # script.test()