def mostrartabla (numero):
    num=int(input("Ingrese un numero"))
    for i in  range (1,11):
        resultado= num * i 
        print(f"{num}x{i}={resultado}")
mostrartabla(6)    