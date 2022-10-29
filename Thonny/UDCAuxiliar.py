print("Éste script mostrará centenas decenas y unidades de un número de tres dígitos")
unidades = 0
decenas = 0
centenas = 0
aux = 0
n = int(input("dame un número de 3 dígitos "))
centenas = n // 100
aux = n - centenas * 100
decenas = aux // 10
unidades = aux - decenas * 10
print("Resultados")
print("Unidades:", unidades)
print("Decenas:", decenas)
print("Centenas:", centenas)
