"""Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima
las líneas del archivo que contienen la cadena recibida."""
def grep(cadena, nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    for linea in archivo:
        if cadena in linea:
            print(linea.strip())
    archivo.close()