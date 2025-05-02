def calificacion ():
    suma=0
    contador=0
    for _ in range (1000):
        num=int(input("Dime tu calificacion "))

        if num != -1:
            suma += num
            contador += 1
        else:
            print("El promedio es de ", suma)
calificacion()