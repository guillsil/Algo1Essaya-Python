"""Juegos sencillos (¡o no tanto!). Estos ejercicios permiten aplicar todo lo aprendido hasta
ahora. Recomendación: pensar bien el diseño; y en particular elegir una estructura
de datos apropiada para representar el estado del juego. Algunas preguntas que pueden ayudar:
• ¿Cómo actualizamos el estado del juego según cada acción realizada?
• ¿Cómo detectamos si un movimiento es válido o no?
• ¿Cómo detectamos si el juego ha terminado?
• ¿Cómo se muestra la información en la consola a los jugadores?
• ¿Cómo hacen los jugadores para ingresar las acciones a realizar?
Escribir un programa que permita jugar1:
a) Torres de Hanói (https://es.wikipedia.org/wiki/Torres_de_Hanoi)
b) Ta-Te-Ti (https://es.wikipedia.org/wiki/Tres_en_linea)
c) Nim (https://es.wikipedia.org/wiki/Nim_(juego))
d) Generala (https://es.wikipedia.org/wiki/Generala)"""
# b)
def tateti():
    tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    jugador = 1
    while True:
        print('Jugador', jugador)
        print('Tablero:')
        for fila in tablero:
            print(fila)
        print('Ingrese la fila y la columna donde quiere poner su ficha')
        fila = int(input('Fila: '))
        columna = int(input('Columna: '))
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = jugador
        else:
            print('Esa casilla ya está ocupada')
            continue
        if jugador == 1:
            jugador = 2
        else:
            jugador = 1
        if (tablero[0][0] == tablero[0][1] == tablero[0][2] != 0) or (tablero[1][0] == tablero[1][1] == tablero[1][2] != 0) or (tablero[2][0] == tablero[2][1] == tablero[2][2] != 0) or (tablero[0][0] == tablero[1][0] == tablero[2][0] != 0) or (tablero[0][1] == tablero[1][1] == tablero[2][1] != 0) or (tablero[0][2] == tablero[1][2] == tablero[2][2] != 0) or (tablero[0][0] == tablero[1][1] == tablero[2][2] != 0) or (tablero[0][2] == tablero[1][1] == tablero[2][0] != 0):
            print('Ganó el jugador', jugador)
            break
        if 0 not in tablero[0] and 0 not in tablero[1] and 0 not in tablero[2]:
            print('Empate')
            break
tateti()

