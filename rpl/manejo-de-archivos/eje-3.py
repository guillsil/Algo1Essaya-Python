"""Escribir una función, llamada cp, que copie todo el contenido de un archivo llamado archivo_origen (sea de texto o binario) a otro llamado archivo_destino, de modo que quede exactamente igual.

Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes."""
def cp(archivo_origen, archivo_destino):
    archivo_origen = open(archivo_origen, 'r')
    archivo_destino = open(archivo_destino, 'w')
    for linea in archivo_origen:
        archivo_destino.write(linea)
    archivo_origen.close()
    archivo_destino.close()
cp("archivo.txt", "archivo2.txt")