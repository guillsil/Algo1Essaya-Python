"""Se tiene una lista de listas que representa un laberinto en forma de matriz (dos dimensiones). En
cada posición $i, j$ habrá una tupla que indicará cuantos casilleros moverse y en qué dirección, por
ejemplo (3,'v') debe moverse 3 posiciones en sentido vertical hacia abajo; (-1, 'h') indica que se debe
mover en una posición hacia la izquierda. Implementar una función que reciba un laberinto de este tipo y
que empezando por el 0, 0 indique en cuántos pasos se sale del laberinto, es decir, llegar a la posición
$n-1, n-1$ (está garantizado que se puede salir)."""
def laberinto(laberinto):
    pasos = 0
    i = 0
    j = 0
    try:
        while True:
            pasos += 1
            if laberinto[i][j][1] == 'h':
                j += laberinto[i][j][0]
            else:
                i += laberinto[i][j][0]
    except IndexError:
        return pasos
print(laberinto([[(1, 'v'), (1, 'h'), (1, 'h')], [(1, 'v'), (1, 'h')], [(1, 'v'), (1, 'v'), (1, 'v')]]))
