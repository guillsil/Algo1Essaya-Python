"""Escribir una función, llamada head que reciba un archivo y un número N e im-
prima las primeras N líneas del archivo."""
def head(archivo, n):
    with open(archivo, 'r') as f:
        for i in range(n):
            print(f.readline())
head('archivo.txt', 3)
