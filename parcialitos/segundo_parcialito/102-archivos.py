"""Se tiene un archivo de valores separados por comas con los siguientes campos: Provincia,Ciudad,Habitantes.
Escribir una función que reciba la ruta de este archivo y el nombre de una provincia, y devuelva la cantidad
total de habitantes que hay en ella.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos
deben quedar cerrados.
"""
def habitantes_provincia(archivo, provincia):
    try:
        archivo = open(archivo, "r")
        habitantes = 0
        for linea in archivo:
            linea = linea.strip()
            linea = linea.split(",")
            if linea[0] == provincia:
                habitantes += int(linea[2])
        archivo.close()
        return habitantes
    except:
        archivo.close()
        return "Error"