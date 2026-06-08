import random
numero_secreto = random.randint(1, 10)
intentos = 0
print("Adivina el numero del 1 al 10")
while True:
    try:
        intento = int(input("Tu numero:  "))
        intentos +=1 
        if intento == numero_secreto:
            print("Correcto lo adivinaste en", intentos, "intentos")
            break
        elif intento < numero_secreto:
            print("Más grande...")
        else:
            print("Más chico...")
    except:
            print("ingresa un numero valido")    