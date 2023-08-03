"""Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima
las líneas del archivo que contienen la cadena recibida."""
def grep(cadena, archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            if cadena in linea:
                print(linea)
grep('2022, baby', 'archivo.txt')
