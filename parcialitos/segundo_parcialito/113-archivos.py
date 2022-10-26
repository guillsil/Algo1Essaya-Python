"""Se posee un archivo con la información de viviendas del censo de Argentina. El archivo no tiene encabezado,
no tiene orden particular y cada línea tiene formato <provincia>;<direccion>;<tipo_vivienda>. Escribir una
función que dado el nombre del archivo, lo procese y escriba en otro archivo cantidad_viviendas.csv un resumen
de la cantidad de viviendas por provincia y tipo, con el formato <provincia>;<tipo_vivienda>;<cantidad>. Por ejemplo,
para el archivo dado informe_viviendas.csv, deberá generarse el siguiente archivo cantidad_viviendas.csv:
informe_viviendas.csv                             cantidad_viviendas.csv
-----                                             ------
Buenos Aires;Las Heras 203;Casa                   Mendoza;Casa;1
Mendoza;Granaderos 300;Casa                       Buenos Aires;Departamento;2
Buenos Aires;Pueyrredón 1004;Departamento         Buenos Aires;Casa;1
Buenos Aires;Roldan 201;Departamento              Cordoba;Oficina;1
Cordoba;Corrientes 1417;Oficina
Aclaraciones: No entra en memoria todas las líneas del archivo original. Se sabe que la cantidad de lineas a
guardar en el destino siempre entran en memoria. No hace falta que el archivo destino mantenga un orden particular
en sus líneas."""

def procesar_archivo(archivo_origen):
    """Recibe el nombre de un archivo de texto con el formato <provincia>;<direccion>;<tipo_vivienda> y
    devuelve un archivo nuevo con el formato {<provincia>: {<tipo_vivienda>: <cantidad>}}"""
    with open(archivo_origen, "r") as archivo:
        diccionario = {}
        for linea in archivo:
            provincia, direccion, tipo_vivienda = linea.strip().split(";")
            if provincia not in diccionario:
                diccionario[provincia] = {}
            if tipo_vivienda not in diccionario[provincia]:
                diccionario[provincia][tipo_vivienda] = 0
            diccionario[provincia][tipo_vivienda] += 1
    return diccionario

def escribir_archivo(diccionario):
    """Recibe un diccionario con el formato {<provincia>: {<tipo_vivienda>:
    <cantidad>}} y escribe en el archivo de texto las lineas <provincia>;<tipo_vivienda>;<cantidad>"""
    with open("cantidad_viviendas.csv", "w") as archivo:
        for provincia, dicc in diccionario.items():
            for tipo_vivienda, cantidad in dicc.items():
                archivo.write(f"{provincia};{tipo_vivienda};{cantidad};\n")
    return archivo
print(escribir_archivo(procesar_archivo("informe_viviendas.csv")))

