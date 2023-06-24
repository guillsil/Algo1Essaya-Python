"""Dado un archivo que registra las ventas de entradas de los partidos del mundial en formato csv el cual contiene las columnas nombre_comprador,equipo1,equipo2, escribir una función que devuelva al equipo mas popular del mundial según cantidad de ventas. Cada fila del archivo corresponde a una entrada vendida y el mismo no posee encabezado. Si hay más de un equipo con la mayor cantidad de ventas, debe devolverse cualquiera de ellos."""
import csv
def equipoMasPopular(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        archivo_csv = csv.reader(archivo)
        ventas = {}
        for nombre, equipo1, equipo2 in archivo_csv:
            if equipo1 not in ventas:
                ventas[equipo1] = 0
            if equipo2 not in ventas:
                ventas[equipo2] = 0
            ventas[equipo1] += 1
            ventas[equipo2] += 1
        print(f"El equipo mas popular es: {max(ventas, key=ventas.get)} con {ventas[max(ventas, key=ventas.get)]} ventas")
        return None
    
print(equipoMasPopular("entradas.csv"))