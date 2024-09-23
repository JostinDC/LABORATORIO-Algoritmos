# Palíndromo: Escribe un programa que verifique si una cadena dada por el usuario es un 
# palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). 

cadena = input("Introduce una cadena: ")

cadena = cadena.replace(" ", "").lower()

palindromo = cadena == cadena[::-1]

if palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
