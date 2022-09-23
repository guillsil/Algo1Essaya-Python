"""Escribir un programa que pida al usuario que ingrese líneas de texto, hasta que ingrese una línea vacía.
El programa deberá imprimir todas las líneas encerradas en un marco. Ejemplo:
Ingrese una linea o enter para terminar: Hola
Ingrese una linea o enter para terminar: Mundo
Ingrese una linea o enter para terminar: en un marco
Ingrese una linea o enter para terminar:
***************
* Hola        *
* Mundo       *
* en un marco *
***************"""
def pedir_lineas():
    """Pide líneas al usuario hasta que ingrese una línea vacía"""
    lista = []
    linea = input("Ingrese una linea o enter para terminar: ")
    while linea != "":
        lista.append(linea)
        linea = input("Ingrese una linea o enter para terminar: ")
    return lista
def obtener_maximo(lista):
    """Obtiene el máximo de la longitud de las cadenas de la lista"""
    maximo = 0
    for linea in lista:
        if len(linea) > maximo:
            maximo = len(linea)
    return maximo
print(obtener_maximo(pedir_lineas()))

def imprimir_marco(lista):
    """Imprime las líneas encerradas en un marco"""
    maximo = obtener_maximo(lista)

    print("*" * (maximo + 4))
    for linea in lista:
        print("*", linea, " " * (maximo - len(linea)), "*", sep="")
    print("*" * (maximo + 4))
imprimir_marco(pedir_lineas())