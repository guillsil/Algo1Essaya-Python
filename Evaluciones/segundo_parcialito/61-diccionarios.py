"""Dada una partida en forma de una lista de tuplas de la forma <personaje>,<movimiento> y un número k,
imprimir por pantalla todos los movimientos notables de cada personaje y cuántas veces se usaron. Se dice que un
movimiento es notable si el personaje lo utilizó más de k veces durante la partida. Ejemplo:
#>>> movimientos = [("Pikachu", "Impactrueno"), ("Charizard", "Lanzallamas"),
                   ("Pikachu", "Ataque Rápido"), ("Charizard", "Lanzallamas")]
#>>> imprimir_notables(movimientos, 1)
Charizard - Lanzallamas (2)
"""
def imprimir_notables(movimientos, k):
    diccionario = {}
    for tupla in movimientos:
        personaje = tupla[0]
        movimiento = tupla[1]
        if personaje not in diccionario:
            diccionario[personaje] = {movimiento: 1}
        else:
            if movimiento not in diccionario[personaje]:
                diccionario[personaje][movimiento] = 1
            else:
                diccionario[personaje][movimiento] += 1
    for personaje in diccionario:
        for movimiento in diccionario[personaje]:
            if diccionario[personaje][movimiento] > k:
                print(personaje, '-', movimiento, '(', diccionario[personaje][movimiento], ')', sep='')
print(imprimir_notables([("Pikachu", "Impactrueno"), ("Charizard", "Lanzallamas"), ("Pikachu", "Ataque Rápido"), ("Charizard", "Lanzallamas")], 1))

