# Escribe un script que solicite al usuario que introduzca el número de años. Calcula el número de 
# segundos que una persona puede vivir. Supongamos que una persona puede vivir cien años.

num_años = int(input("Introduzca el número de años: "))

segundos_año = 365 * 24 * 60 * 60

vida_segundos = num_años * segundos_año
print("Usted va a vivir por:",vida_segundos,"segundos")