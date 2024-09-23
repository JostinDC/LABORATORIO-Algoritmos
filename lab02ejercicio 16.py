# Extraer subcadena: Escribe un programa que extraiga una subcadena de una cadena dada por el usuario, especificando los indices de inicio y fin

cadena = input("Introduce una cadena: ")

inicio = int(input("Introduce el índice de inicio: "))
fin = int(input("Introduce el índice de fin: "))

subcadena = cadena[inicio:fin]
print("La subcadena es:", subcadena)

