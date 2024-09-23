"""Escribe un script que solicite al usuario que introduzca las horas y la tarifa por hora. ¿Cuál es el 
pago de la persona? 
Introduce las horas: 40 
Introduce la tarifa por hora: 28 
Tu salario semanal es 1120"""


hora = int(input("Introduzca las horas: "))
tarifa_hora = int(input("Introduzca la tarifa por hora: "))

salario = hora * tarifa_hora
print("Tu salario semanal es de:",salario)