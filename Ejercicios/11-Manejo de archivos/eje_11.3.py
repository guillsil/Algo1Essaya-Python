"""Escribir una función, llamada wc, que dado un archivo de texto, lo procese e
imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo."""
def wc(archivo):
    with open(archivo, 'r') as f:
        lineas = 0
        palabras = 0
        caracteres = 0
        for linea in f:
            lineas += 1
            palabras += len(linea.split())
            caracteres += len(linea)
        print('El archivo tiene {} lineas, {} palabras y {} caracteres.'.format(lineas, palabras, caracteres))
wc('archivo.txt')