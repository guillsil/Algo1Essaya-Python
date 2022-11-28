"""Escribir un programa que le pida al usuario que ingrese un número entero positivo n y una cadena, e imprima
la misma cadena pero con un guión (-) cada n lugares.
Ejemplo: n = 2, cadena = Esto es un ejemplo.; debe imprimir Es-to- e-s -un- e-je-mp-lo-."""
def imprimir_cadena(n, cadena):
    """Imprime la cadena con un guión cada n lugares"""
    contador = 0
    for caracter in cadena:
        if contador == n:
            print("-", end="")
            contador = 0
        print(caracter, end="")
        contador += 1
imprimir_cadena(2, "Esto es un ejemplo.")