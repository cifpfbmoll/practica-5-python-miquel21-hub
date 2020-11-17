#PRÁCTICA 5 EJERCICIO 8
altura=int(input("Introduce la altura del triángulo\n"))
for i in range(altura):
    for j in range(i+1):
        print("  *  ", end="")
    print()
for i in range(altura):
    for j in range(altura-(i+1)):
        print("  *  ", end="")
    print()