# Contar vocales: Escribe un programa que cuente el número de vocales en una cadena dada por el usuario.

cadena = input("Introduce una cadena: ")

vocales = "AEIOUaeiou"

contador_vocales = 0

for x in cadena:
    if x in vocales:
        contador_vocales += 1
print("El numero de vocales en la cadena es de: ",contador_vocales)
