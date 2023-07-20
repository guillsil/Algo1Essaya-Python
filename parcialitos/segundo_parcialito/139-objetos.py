"""
Para desarrollar un videojuego necesitamos que todos los personajes tengan una cantidad de vida entre 0 y 100, y un valor de daño de ataque. Cuando un personaje ataca a otro, se le resta el daño del atacante a su cantidad de vida. Se dice que un personaje está muerto si su cantidad de vida llega a 0.

Implementar la clase Personaje con los siguientes métodos:

    El constructor recibe el daño que hace su ataque. La cantidad de vida arranca sendo 100.
    esta_muerto() que debe informar si el personaje está muerto
    atacar() que recibe otro personaje. Si alguno de los dos personajes está muerto debe lanzar una excepción. En caso contrario debe atacar al personaje recibido.
    curar() que recibe una cantidad de vida a regenerar. La vida máxima no se modifica. Si el personaje está muerto, debe lanzar una excepción.

"""
class Personaje:
    def __init__(self, daño):
        self.vida = 100
        self.daño = daño