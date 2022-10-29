# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducción no es correcta.

def f(x):
	y = x**4+3*x**3-2
	return y

if __name__ == '__main__':
	print("xi: ", end="")
	xi = float(input())
	print("xd: ", end="")
	xd = float(input())
	intervalovalido = False
	xm = (xi+xd)/2
	print("Iteraciones: ", end="")
	n = float(input())
	print("")
	while True:# no hay 'repetir' en python
		if f(xi)*f(xd)<0:
			intervalovalido = True
			for i in range(n+1):
				if i==0:
					print("Existe una raíz de la función en el intervalo [",xi,", ",xd,"]")
					print("")
				print("Iteración: ",i)
				print("")
				print("xi:",xi, end="")
				print("    xd:",xd, end="")
				print("    xm:(",xi,"+",xd,")/2 = ",xm)
				print("f(xi):",f(xi), end="")
				print("    f(xd):",f(xd), end="")
				print("    f(xm):",f(xm))
				print("")
				if f(xd)*f(xm)<0:
					print("Caso 1: ")
					print("f(xd)*f(xm) < 0")
					print("Entonces xi <- xm y xm se vuelve a calcular usando la misma fórmula, pero con los nuevos datos")
					xi = xm
					xm = (xi+xd)/2
				else:
					if f(xd)*f(xm)>0:
						print("Caso 2: ")
						print("f(xd)*f(xm) > 0")
						print("Entonces xd <- xm y xm se vuelve a calcular usando la misma fórmula, pero con los nuevos datos")
						xd = xm
						xm = (xi+xd)/2
				print("")
				print("Nuevos datos al terminar la iteración: ")
				print("xm: ",xm, end="")
				print("    f(xm):",f(xm))
				print("______________________________________________________________________________________________")
		else:
			intervalovalido = False
		if intervalovalido: break

