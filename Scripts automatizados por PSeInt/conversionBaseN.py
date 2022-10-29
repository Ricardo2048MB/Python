# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import log

if __name__ == '__main__':
	print("")
	print("Éste programa convertirá un número base 10 en su equivalente de base N")
	print("")
	print("Escribe un número natural ", end="")
	n = int(input())
	print("Escribe la base a la que quieres convertir el número ", end="")
	base = float(input())
	if n==0:
		print("")
		print("El que es perico en donde quiera es verde")
		print("")
	else:
		if n<0:
			print("")
			print("El logaritmo de un número negativo no está definido en los reales")
			print("")
		else:
			m = n
			pos = int(log(n)/log(base))+1
			sistema = [float() for ind0 in range(pos)]
			for i in range((pos-1),-1,-1):
				if n!=0:
					sistema[i] = n%base
					n = int(n/base)
			print("")
			print("El número ",m," convertido a la base ",base," es: ", end="")
			for i in range(pos):
				print(sistema[i],"|", end="")
			print("")
			print("")

