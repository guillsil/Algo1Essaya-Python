"""Escribir un programa que le pregunte al usuario dos números enteros y luego devuelva una lista con
todos los números pares que se encuentren en el rango definido por estos dos números (incluyendo ambos).
El programa debe validar que el usuario ingrese números enteros, volviéndole a pedir un nuevo número hasta
que el ingresado cumpla con las restricciones.
"""
def pedir_numero():
    """Pide un número entero al usuario"""
    numero = input("Ingrese un número entero: ")
    while not numero.isdigit():
        numero = input("Ingrese un número entero: ")
    return int(numero)

def pedir_rango():
    """Pide un rango de números al usuario"""
    numero1 = pedir_numero()
    numero2 = pedir_numero()
    return numero1, numero2

def obtener_pares(rango):
    """Obtiene los números pares del rango"""
    lista = []
    for numero in range(rango[0], rango[1] + 1):
        if numero % 2 == 0:
            lista.append(numero)
    return lista

def main():
    """Función principal"""
    print(obtener_pares(pedir_rango()))
main()