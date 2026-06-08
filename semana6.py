# Agregar una tarea al archivo
tarea = input("Escribí una tarea: ")
with open("tareas.txt",  "a" ) as archivo:
    archivo.write(tarea + "\n")
# Leer todas las notas guardadas
print("\ntus tareas guardadas:")
with open("tareas.txt",  "r")as archivo:
    for linea in archivo:
        print("-", linea.strip())
