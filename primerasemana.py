numero_secreto = 7
while True:
    intento = int(input("adivina el numero de 1 al 10: "))
    if intento == numero_secreto:
        print("Correcto!! adivinaste!!")
        break
    elif intento < numero_secreto:
        print ("mas grande..")
    else:
        print ("mas chico..")
        