#PRÁCTICA 5 EJERCICIO 3
#Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.
NÚMERO_1=int(input("Introduzca 1 número"))
NÚMERO_2=int(input("Introduzca otro número mayor al primero"))
if(NÚMERO_1>=NÚMERO_2):
    print("Le he pedido 1 número mayor")
else:
    suma=0
    for x in range(NÚMERO_1,NÚMERO_2+1):
        suma= suma+x
    print("Es", suma)