#PRÁCTICA 5 EJERCICIO 2
#Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares\
# y cuáles impares.
Numero_1=int(input("Ponga un número\n"))
Numero_2=int(input("Ponga otro número que sea mayor al primero\n"))
if Numero_1>Numero_2 :
    print("El segundo número tiene que ser mayor!")
else :
    for x in range(Numero_1, Numero_2+1):
        if (x % 2==0):
            print("El número",x, "es par")
        else :
            print("El número",x, "es impar")