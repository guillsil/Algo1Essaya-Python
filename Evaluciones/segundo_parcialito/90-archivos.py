"""Se cuenta con un archivo en formato csv que guarda información de pasajes de avión, respetando
la siguiente estructura: fecha,destino,precio. Escribir una función que dada la ruta del archivo,
devuelva un diccionario cuyas claves sean cada uno de los destinos, y el valor asociado a cada clave
una tupla (fecha, precio) con el pasaje más barato para el destino.
Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben
quedar cerrados.
"""
def pasajes_mas_baratos(archivo):
    try:
        archivo = open(archivo, "r")
        diccionario = {}
        for linea in archivo:
            linea = linea.strip()
            linea = linea.split(",")
            if linea[1] in diccionario:
                if linea[2] < diccionario[linea[1]][1]:
                    diccionario[linea[1]] = (linea[0], linea[2])
            else:
                diccionario[linea[1]] = (linea[0], linea[2])
        archivo.close()
        return diccionario
    except:
        archivo.close()
        return "Error"