print("Dame un número, por favor")
x = int(input())
print("Dame otro número, por favor")
y = int(input())
print("Tus números sumados son: ", x + y)
print("Tus números restados son: ", x - y)
print("Tus números multiplicados son: ", x * y)

if y != 0:
    print("Tus números divididos son: ", x / y)
else:
    print("Tus números divididos no los pude calcular porque no se puede dividir entre cero")