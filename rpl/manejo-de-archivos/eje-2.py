"""Escribir una función, llamada head que reciba un nombre de archivo y un número N e imprima las primeras N
líneas del archivo.
Solo completar la función del archivo head.py!"""
def head(nombre_archivo, n):
    archivo = open(nombre_archivo, 'r')
    for i in range(n):
        print(archivo.readline().strip())
    archivo.close()

#completar un archivo n cantidad de veces con la cadena "guillermo es el {i} mejor programador del mundo"
def completar_archivo(nombre_archivo, n):
    archivo = open(nombre_archivo, 'w')
    for i in range(n):
        archivo.write(f"guillermo es el {i} mejor programador del mundo\n")
    archivo.close()
completar_archivo("archivo.txt", 21)
