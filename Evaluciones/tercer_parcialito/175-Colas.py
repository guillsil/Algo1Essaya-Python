"""Escribir una función tail, que recibe una ruta a un archivo de texto y un número n, y que imprima por pantalla
las últimas n líneas del archivo. No está permitido almacenar todo el archivo en memoria ni recorrer el archivo
más de una vez."""

def tail(archivo, n):
    with open(archivo, "r") as f:
        for i in range(n):
            f.readline()
        for linea in f:
            print(linea)
