def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir (a, b):
    if b == 0:
        return "error: no se puede dividir por cero"
    return a/b
#menu
print("1. sumar  2.restar  3.multiplicar  4. dividir")
opcion = input("elegí una opcion:" )
a = float(input("primer numero"))
b = float(input("segundo numero"))
if opcion == "1":
    print("resultado:", sumar(a, b))
elif opcion == "2":
    print("resultado:", restar(a, b))
elif opcion == "3":
    print("resultado:", multiplicar(a, b))
elif opcion == "4":
    print("resultado:", dividir (a, b))
