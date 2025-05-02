def numeros_fibonacci ():
    n=int(input("Cuantos numeros deseas ver "))
    a, b= 0, 1

    for i in range (n):
        print (a)
        a , b= b,  a + b
numeros_fibonacci()