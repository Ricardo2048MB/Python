numero = int(input())
centenas = numero // 100
print(centenas)
decenas = (numero - centenas)  // 10
print(decenas)
unidades = numero - (centenas + decenas * 10)
print(unidades)

