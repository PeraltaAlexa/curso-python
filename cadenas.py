dato = (input ("introduce texto: "))
text = dato
conteo = 0
for letra in text:
	dato2 = (input("introduzca la letra a contar"))
	if letra == dato2:
		conteo += 1
print(" el dato ", text, " tiene ", conteo, " letras ",dato2)
print(dato.upper())
print(" la longitud de la cadena es de ", len(dato))
