#PRÁCTICA 5 EJERCICIO 9
anchura=int(input("Introduce la anchura del rectángulo\n"))
altura=int(input("Introduce la altura del rectángulo"))
for i in range(altura):
    for j in range(anchura):
        print(" * ", end="")
    print()