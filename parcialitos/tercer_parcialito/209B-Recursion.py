"""Alan, Bárbara y Grace juegan al ping-pong. El que gana un partido sigue jugando, mientras que el que lo pierde es reemplazado por el que no jugaba. El primer partido es entre Romeo y Dante. Se gana una cerveza el primero que gana tres partidos seguidos. Implementar una función recursiva que simule este juego y devuelva quien ganó. Suponer que la probabilidad de ganar un partido es igual para ambos.

Nota: para simular el resultado de cada parido en forma aleaoria, utilizar la función random.choice.
"""
import random 
#iterativa
def ping_pong():
    jugadores = ["Alan", "Bárbara", "Grace"]
    ganador = random.choice(jugadores)
    while True:
        perdedor = random.choice(jugadores)
        if perdedor != ganador:
            break
    jugadores.remove(perdedor)
    jugadores.append(ganador)
    if jugadores.count(ganador) == 3:
        return ganador
    else:
        return ping_pong()
print(ping_pong())
#recursiva
def ping_pong2(jugadores):
    import random

def ping_pong(jugador1, jugador2, ganador_anterior=None, ganados=0):
    if ganados == 3:
        return ganador_anterior
    else:
        if ganador_anterior == jugador1:
            ganador = jugador2
        elif ganador_anterior == jugador2:
            ganador = jugador1
        else:
            ganador = random.choice([jugador1, jugador2])
        return ping_pong(jugador1, jugador2, ganador, ganados + 1 if ganador == ganador_anterior else 1)

print(ping_pong("Romeo", "Dante"))
