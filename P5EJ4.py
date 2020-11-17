#PRÁCTICA 5 EJERCICIO 4
#Escribe un programa que pida un número y calcule su factorial.
a=int(input("Introduce un número positivo para calcular su factorial"))
if (a<=0):
    print ("¡Introduza un número positivo!")
else:
    factorial=1
    for i in range (a):
        factorial= factorial * (i+1)
print (factorial)
