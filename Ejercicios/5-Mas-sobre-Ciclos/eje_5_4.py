"""Utilizando la función randrange del módulo random, escribir un programa que
obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
correcto."""
import random
def adivinar():
    n = random.randrange(1, 100)
    ingreso = int(input("Ingrese un numero: "))
    contador = 0
    while ingreso != n:
        if ingreso > n:
            print("El numero es menor")
            contador += 1
        else:
            print("El numero es mayor")
            contador += 1
        ingreso = int(input("Ingrese un numero: "))
    print("El numero es correcto")
    return contador
print(adivinar())