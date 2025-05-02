def multiplicacion(numero):
    numero=int(input("La tabla del numero: "))
    for i in range (1,11):
        tabla= numero * i 
        print(f"{numero} x {i} = {tabla}")
multiplicacion(numero=0)