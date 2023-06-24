"""Se tiene un archivo CSV de cuatro columnas, “Equipo”, “Jugador”, “Fecha” y “Goles”. El archivo está ordenado por equipo y, dentro de cada equipo, por jugador.

Se pide implementar una función que reciba el nombre del archivo como parámetro, e imprima el total de goles de cada jugador, y de cada equipo.
"""
import csv
def totalGoles(ruta_archivo):
    with open(ruta_archivo) as archivo:
        archivo_csv = csv.reader(archivo)
        golesEquipos = {}
        golesJugadores = {}
        for equipo, jugador, fecha, goles in archivo_csv:
            if equipo not in golesEquipos:
                golesEquipos[equipo] = 0
            if jugador not in golesJugadores:
                golesJugadores[jugador] = 0
            golesEquipos[equipo] += int(goles)
            golesJugadores[jugador] += int(goles)
        for equipo in golesEquipos:
            print(f"El equipo {equipo} hizo {golesEquipos[equipo]} goles")
        for jugador in golesJugadores:
            print(f"El jugador {jugador} hizo {golesJugadores[jugador]} goles")


totalGoles("tabla.csv")
