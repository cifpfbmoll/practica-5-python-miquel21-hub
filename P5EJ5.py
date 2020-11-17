#PRÁCTICA 5 EJERCICIO 5
anchura=int(input("Introduce la anchura del rectangulo\n"))
altura=int(input("Introduce la altura\n"))
for i in range(altura):
    for x in range(anchura):
        print("*", end="")
    print()