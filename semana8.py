import datetime
def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print("No tenés tareas guardadas")
    else:
        print("\--- Tus tareas ---")
        for i, tarea in enumerate(tareas):
            print(i + 1, "-", tarea)
def guardar_tareas(tareas):
    with open("mis_tareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def cargar_tareas():
    tareas = []
    try:
        with open ("mis_tareas.txt",  "r") as archivo:
            for linea in archivo:
                tareas.append(linea.strip())
    except:
        pass
    return tareas
# ---programa principal ---
tareas = cargar_tareas()

while True:
    print("\n¿que querés hacer?")
    print("1 - ver tareas")
    print("2 - Agregar tarea")
    print("3 - eliminar tarea")
    print("4 - salir")

    opcion = input("elegi una opcion:  ")

    if opcion == "1":
        mostrar_tareas(tareas)

    elif opcion == "2":
        nueva = input("Escribí una tarea:  ")
        ahora = datetime.datetime.now().strftime("%d/%m %H:%M")
        tareas.append(nueva + " [" + ahora + "]")
        guardar_tareas(tareas)
        print("tarea agregada!")

    elif opcion == "3":
        mostrar_tareas(tareas)
        if len(tareas) > 0:
            try:
                numero = int(input("¿Cuál querés eliminar? (numero): "))
                tareas.pop(numero - 1)
                guardar_tareas(tareas)
                print("tarea eliminada!")
            except:
                print("Número invalido.")

    elif opcion == "4":
        print("hasta luego!")
        break

    else:
        print("Opción no válida, probá de nuevo. ")


    