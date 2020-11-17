#PRÀCTICA 5 EJERCICIO 10
#Escribe un programa que pida un número e imprima todos sus divisores.
#Primero pedimos que nos introduzca el numero
número=int(input("Introduce el número mayor que cero \n"))
#Luego introducimos la condición de que sea mayor que cero y si no es así le volvemos a pedir que introduzca el número.
if número<=0:
    print("Le he pedido un número mayor que cero")
#Una vez tenemos el numero, hacemos un for i in range que pasará por cada numero desde el 1 hasta el número indicado.
else:
    print("Los divisores de", número, "son")
    for i in range (1,número+1):
#Aquí introducimos una condición para saber si el número es divisible entero.        
        if número % i==0:
            print(i, end=" ")
