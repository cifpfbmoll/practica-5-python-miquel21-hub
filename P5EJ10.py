#PRÁCTICA 5 EJERCICIO 10
altura=int(input("Indica la altura de su triángulo \n"))
for i in range (1,altura+1):
    for j in range(altura-i):
        print("  ", end=" ")
    for j in range (1,2*i):
        print("* ", end=" ")
    print("\n")