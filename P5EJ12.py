#PRÁCTICA 5 EJERCICIO 11
#Escribe un programa que pida un número y escriba si es primo o no.
#Primero pedimos un número mayor que cero e indicamos esa condición.
número=int(input("Introduce un numero mayor que cero \n"))
if número<=0:
    print("¡Tiene que ser mayor que cero!")
#Ahora hacemos un for i in range desde 1 hasta el número indicado y utilizando condiciones analizamos si cada número es primo o compuesto.
else:
    for i in range (1,número+1):
        if i%==int:
            print(i,"no es primo")
        else:
            print(i, "es primo")
