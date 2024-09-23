#Los números pares son divisibles por 2 y el residuo es cero. ¿Cómo comprobarías si un número es par o no usando python?

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número",numero,"es par")
else:
    print("El numero",numero,"es impar")