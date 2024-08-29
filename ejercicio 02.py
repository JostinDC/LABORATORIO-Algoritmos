# COMPARA LA LONGITUD DE TU NOMBRE Y APELLIDO

nombre=input("Ingresa tu nombre por favor: ")
apellido=input("Ingresa tu apellido por favor: ")

long_nombre=len(nombre)
long_apellido=len(apellido)

if long_nombre > long_apellido:
    print("Tu nombre",nombre,"es mas largo que tu apellido",apellido)
elif long_apellido > long_nombre:
    print("Tu apellido",apellido,"es mas largo que tu nombre",nombre)
else:
    print("Tu nombre",nombre,"y tu apellido",apellido,"tienen la misma longitud")
    
    # "Tu nombre",nombre,"y tu apellido" es igual a "Tu nombre {nombre} y tu apellido"
    # no hay necesidad de estar abriendo y cerrando comillas