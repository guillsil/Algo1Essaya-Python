"""Se tiene un archivo de valores separados por comas con los siguientes campos: Gundam,Parte,Peso.
Escribir una función que reciba la ruta de este archivo y el nombre de una Gundam, y devuelva el peso total del mismo.
Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""
def peso_gundam(archivo, gundam):
    try:
        archivo = open(archivo, "r")
        peso_total = 0
        for linea in archivo:
            linea = linea.strip()
            linea = linea.split(",")
            if linea[0] == gundam:
                peso_total += int(linea[2])
        archivo.close()
        return peso_total
    except:
        archivo.close()
        return "Error"
print(peso_gundam("gundams.txt", "Gundam1"))