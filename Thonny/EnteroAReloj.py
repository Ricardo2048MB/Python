##Programa que lee el número de segundos y muestra su equivalente en horas, minutos y segundos
n = int(input("Por favor escribe el número de segundos para convertirlos a hms "))
h = 0
m = 0
s = 0
s = n % 60
n = n // 60
m = n % 60
n = n // 60
h = n % 60
print(h, ":", m, ":", s)