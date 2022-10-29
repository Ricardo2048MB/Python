print("Éste script mostrará las unidades decenas y centenas de un número de 3 dígitos que escribas")
unidades = 0
decenas = 0
centenas = 0
n = int(input("\nPor favor escribe un número de 3 dígitos y presiona enter "))
centenas = n // 100
n = n - centenas * 100
decenas = n // 10
n = n - decenas * 10
unidades = n
print("Resultados")
print("Unidades:", unidades)
print("Decenas:", decenas)
print("Centenas:", centenas)
