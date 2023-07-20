"""Escribir dos funciones:

    leer_primera_linea(nombre_archivo): Devuelve el contenido de la primer línea del archivo, sin el salto de línea si lo tiene.

    escribir_en_archivo(contenido, nombre_archivo): Escribe el valor de contenido al archivo nombre_archivo, reemplazando su contenido existente.

Para la sintaxis básica de archivos en Python, consultar el apunte teórico de la materia en la sección 11 Manejo de archivos

Ejemplo de uso:

>>> escribir_en_archivo('Hola!', 'archivo.txt')
>>> linea = leer_primera_linea('archivo.txt')
>>> print(linea)
Hola!"""
def leer_primera_linea(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    linea = archivo.readline()
    archivo.close()
    return linea.strip()
print(leer_primera_linea('archivo.txt'))

def escribir_en_archivo(contenido, nombre_archivo):
    archivo = open(nombre_archivo, 'w')
    archivo.write(contenido)
    archivo.close()
(escribir_en_archivo('ANAANNANANANNANANANANNANANANNANAN', 'archivo.txt'))
print(leer_primera_linea('archivo.txt'))

