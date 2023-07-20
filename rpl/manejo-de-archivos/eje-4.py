"""Escribir una función, llamada wc, que dado un archivo de texto, lo procese e imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.

Por ejemplo:

#>>> head('test_file', 10)
Soy la línea 1
Soy la línea 2
Soy la línea 3
#>>> wc('test_file')
Cantidad de líneas: 3
Cantidad de palabras: 12
Cantidad de caracteres: 44

Nota: El contador de caracteres incluye espacios y saltos de línea."""
def wc(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    lineas = 0
    palabras = 0
    caracteres = 0
    for linea in archivo:
        lineas += 1
        palabras += len(linea.split())
        caracteres += len(linea)
    print(f"Cantidad de lineas: {lineas}")
    print(f"Cantidad de palabras: {palabras}")
    print(f"Cantidad de caracteres: {caracteres}")
    archivo.close()
wc("archivo.txt")