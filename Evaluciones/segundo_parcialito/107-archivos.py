"""Se tiene un archivo CSV de cuatro columnas, “Equipo”, “Jugador”, “Fecha” y “Goles”. El archivo está ordenado
por equipo y, dentro de cada equipo, por jugador.
Se pide implementar una función que reciba el nombre del archivo como parámetro, e imprima el total de goles
de cada jugador, y de cada equipo.
"""
def goles_por_equipo_y_jugador(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    archivo.readline() # Salteo la primera linea
    equipo = ''
    jugador = ''
    goles = 0
    for linea in archivo:
        datos = linea.strip().split(',')
        if datos[0] != equipo:
            if equipo != '':
                print('Total de goles del equipo {}: {}'.format(equipo, goles))
            equipo = datos[0]
            jugador = datos[1]
            goles = int(datos[3])
        elif datos[1] != jugador:
            print('Total de goles del jugador {}: {}'.format(jugador, goles))
            jugador = datos[1]
            goles = int(datos[3])
        else:
            goles += int(datos[3])
    print('Total de goles del jugador {}: {}'.format(jugador, goles))
    print('Total de goles del equipo {}: {}'.format(equipo, goles))
    archivo.close()
goles_por_equipo_y_jugador('goles.csv')
