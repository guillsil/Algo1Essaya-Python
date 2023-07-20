"""Escribir una función, llamada rot13, que reciba un archivo de texto de origen y uno de destino, de modo que
para cada línea del archivo origen, se guarde una línea cifrada en el archivo destino.

El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido entre la a y la z, se le
suma 13 (a su posición en el conjunto "a hasta la z") y luego se aplica el módulo 26, para obtener un nuevo caracter.

Por ejemplo, el contenido del archivo origen es:

escribir una funcion, rot13
que reciba un archivo de texto

El archivo destino debe tener:

rfpevove han shapvba, ebg13
dhr erpvon ha nepuvib qr grkgb"""
def rot13(archivo_origen, archivo_destino):
    archivo_origen = open(archivo_origen, 'r')
    archivo_destino = open(archivo_destino, 'w')
    for linea in archivo_origen:
        "a cada caracter comprendido entre la a y la z, se le suma 13 (a su posición en el conjunto 'a hasta la z') " \
        "y luego se aplica el módulo 26, para obtener un nuevo caracter."
        for caracter in linea:
            if caracter.isalpha() and caracter.islower():
                caracter = chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
            archivo_destino.write(caracter)
    archivo_origen.close()
    archivo_destino.close()
rot13("archivo3.txt", "archivo2.txt")

