"""Escribir un programa que le pida al usuario que ingrese una sucesión de números
naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de
salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total
de los valores y el promedio."""
def sucesion():
    ingreso = int(input("Ingrese un numero: "))
    contador = 0
    suma = 0
    while (ingreso != -1):
        suma += ingreso
        contador += 1
        ingreso = int(input("Ingrese un numero: "))
    return contador, suma, suma/contador
print(sucesion())