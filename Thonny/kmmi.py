KMMI = 0.621371
print("Éste script convierte km a mi y viceversa")
valido = False
opcion = 0
x = 0
y = 0
while not valido:
    print("Selecciona una opción")
    print("1. km a mi")
    print("2. mi a km")
    opcion = int(input())
    if opcion == 1:
        print("De kilómetros a millas")
        x = int(input("km: "))
        y = x * KMMI
        print(x, "km son", y, "mi")
        valido = True
    elif opcion == 2:
        print("De millas a kilómetros")
        x = int(input("mi: "))
        y = x / KMMI
        print(x, "mi son", y, "km")
        valido = True

    
    
