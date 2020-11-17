#PRÁCTICA 5 EJERCICIO 6
altura=int(input("Dígame la altura de su triangulo\n"))
for i in range(altura):
    for j in range(i+1):
        print("*", end="")
    print()