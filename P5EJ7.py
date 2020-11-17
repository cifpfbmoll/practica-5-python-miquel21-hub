#PRÁCTICA 5 EJERCICIO 7
altura=int(input("Introduce la altura del triángulo\n"))
for i in range(altura):
    for j in range(altura-i):
        print("*", end="")
    print()