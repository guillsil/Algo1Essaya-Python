"""Dado un archivo con el siguiente encabezado: Día,Mes,Año,Rubro,Gasto, ordenado cronológicamente
(el gasto más reciente está al final): escribir una función que reciba el nombre de archivo y dos tuplas de la
forma (mes, año). La función debe devolver el nombre del rubro que más gastos lleva acumulados entre las fechas
dadas y dicho gasto acumulado.
Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar
cerrados.
"""
def rubro_mas_gastado(archivo, fecha1, fecha2):
    try:
        archivo = open(archivo, "r")
        archivo.readline()
        rubro_mas_gastado = ""
        gasto_mas_alto = 0
        for linea in archivo:
            linea = linea.strip()
            linea = linea.split(",")
            if (int(linea[1]), int(linea[2])) >= fecha1 and (int(linea[1]), int(linea[2])) <= fecha2:
                if int(linea[4]) > gasto_mas_alto:
                    gasto_mas_alto = int(linea[4])
                    rubro_mas_gastado = linea[3]
        archivo.close()
        return rubro_mas_gastado, gasto_mas_alto
    except:
        archivo.close()
        return "Error"
    