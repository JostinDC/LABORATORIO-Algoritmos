# Clasificación de Triángulos: 
# Escribe un programa que pida al usuario las longitudes de tres lados de un triángulo y 
# determine si es equilátero, isósceles o escaleno. 

long_lado1 = float(input("Ingrese la longitud del primer lado: "))
long_lado2 = float(input("Ingrese la longitud del segundo lado: "))
long_lado3 = float(input("Ingrese la longitud del tercer lado: "))


if long_lado1 == long_lado2 == long_lado3:
    print("El triangulo es equilátero.")
elif long_lado1 == long_lado2 or long_lado1 == long_lado3 or long_lado2 == long_lado3:
    print("El triangulo es isósceles.")
else:
    print("El triangulo es escaleno.")