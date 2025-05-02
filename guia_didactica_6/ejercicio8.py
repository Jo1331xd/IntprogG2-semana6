def saludo():
    print("Hola, que tal tu día? ")

def mostrar():
    print("La fecha actual es 01/05/2025")

def menu():
    print("="*40)
    print("""Bienvenido al menu
          - Saludar
          - Mostrar
          - Salir""")
    print("="*40)

    opcion=input("")


    if opcion=="Saludar":
        saludo()
        for _ in range (1):
            menu()
    elif opcion=="Mostrar":
        mostrar()
        for _ in range (1):
            menu()
    elif opcion=="Salir":
        
        print("="*20)
        print("Adios")
        print("="*20)


menu()
    

