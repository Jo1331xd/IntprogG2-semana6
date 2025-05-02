def sumar_hasta ():
    suma=0
    contador=0
    for _ in range(1000):
        num=int(input("Dame un numero "))
        suma += num
        contador += 1
        if suma >=100:
            print ("Has sobre pasado el limite ", "Suma total: ", suma)
sumar_hasta()