"""Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usua-
rio, a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1-Conceptos-Basicos.5) e imprima
el resultado junto con el número de orden correspondiente."""
from eje_1_5 import factorial

def main():
    print("Ingresa los numeros que quiere ver sus factoriales, separado por un espacio")
    array = list(map(int, input().split()))
    max=len(array)
    for i in range(max):
        print(factorial(array[i]))
main()
