tareas = []

tareas.append("Estudiar pyhton")
tareas.append("Hacer ejercicio")
tareas.append("Leer 30 min")
print("Mis tareas de hoy:")
for tarea in tareas:
    print("-", tarea)
print("total de tareas:", len(tareas))

tareas.remove("Hacer ejercicio")
print("\nDespues de eliminar:")
for tarea in tareas:
    print("-", tarea)
print("total de tareas:", len(tareas))

