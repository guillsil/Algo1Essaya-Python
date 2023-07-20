"""Escribir un programa que pida dos números enteros al usuario (a y b) e imprima los primeros a múltiplos
de b. El programa debe validar que cada número que ingrese el usuario sea un entero positivo y, en caso
de que no lo sea, solicitarlo nuevamente (hasta que se ingrese algo correcto)."""

def pedir_entero_positivo():
    """Pide al usuario que ingrese un entero positivo"""
    while True:
        numero = input("Ingrese un entero positivo: ")
        if numero.isdigit():
            return int(numero)
        print("Debe ingresar un entero positivo.")

def imprimir_multiplos(a, b):
    """Imprime los primeros a múltiplos de b"""
    for i in range(1, a + 1):
        print(i * b)

def main():
    """Función principal"""
    a = pedir_entero_positivo()
    b = pedir_entero_positivo()
    imprimir_multiplos(a, b)
main()