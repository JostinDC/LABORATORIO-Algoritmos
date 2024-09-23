#  Verificar prefijo y sufijo: Escribe un programa que verifique si una cadena dada por el usuario 
#  comienza con un prefijo específico y termina con un sufijo específico.

cadena = input("Introduzca una cadena: ")

prefijo = input("Introduzca el prefijo: ")
sufijo = input("Introduzca el sufijo: ")

cadena_empiezapref = cadena.startswith(prefijo)
cadena_terminasuf = cadena.endswith(sufijo)

if cadena_empiezapref:
    print("La cadena si empieza con el prefijo:",prefijo)
else:
    print("La cadena no empieza con el prefijo:",prefijo)
    
if cadena_terminasuf:
    print("La cadena termina con el sufijo:",sufijo)
else:
    print("La cadena no termina con el sufijo:",sufijo)