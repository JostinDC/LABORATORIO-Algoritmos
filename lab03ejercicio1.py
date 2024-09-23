# Orden Alfabético: 
# Escribe un programa que solicite al usuario dos palabras y determine cuál va primero en orden 
# alfabético.

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if palabra1 < palabra2:
    print(f"La palabra {palabra1} va primero en orden alfabético.")
else:
    print(f"La palabra {palabra2} va primero en orden afabético.")