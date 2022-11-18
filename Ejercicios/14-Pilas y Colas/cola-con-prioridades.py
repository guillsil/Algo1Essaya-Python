"""Este es un ejercicio parecido al 14.5:
Sabiendo que se cuenta con una clase Cola con las primitivas encolar, desencolar y esta_vacia, implementar la clase
ColaConPrioridad. Este nuevo tipo debe tener los métodos encolar(elemento), encolar_prioritario(elemento), desencolar(),
ver_primero y esta_vacia(); y al desencolar debe priorizar aquellos elementos que fueron encolados con prioridad;
es decir, no deben salir elementos comunes de la estructura si no salieron previamente todos los elementos con prioridad.
Antes de pensar en nodos y estructuras internas, vemos que lo descripto es muy similar a una Cola tradicional con el
detalle de elementos prioritarios.
Podemos pensar esto con dos colas . En una agregamos los elementos que se encolan normalmente, y en la otra agregamos
los elementos encolados con prioridad. A la hora de desencolar, primero evaluamos la cola con prioridad. """
from cola import Cola


class ColaConPrioridad:
	def __init__(self):
		self.normales = Cola()
		self.prioritarios = Cola()

	def encolar_prioritario(self, elemento):
		self.prioritarios.encolar(elemento)

	def encolar(self, elemento):
		self.normales.encolar(elemento)

	def desencolar(self):
		if not self.prioritarios.esta_vacia():
			return self.prioritarios.desencolar()
		return self.normales.desencolar()

	def ver_primero(self):
		if not self.prioritarios.esta_vacia():
			return self.prioritarios.ver_primero()
		return self.normales.ver_primero()

	def esta_vacia(self):
		return self.normales.esta_vacia() and self.prioritarios.esta_vacia()


cola_prioridad = ColaConPrioridad()

cola_prioridad.encolar(3)
cola_prioridad.encolar(4)
cola_prioridad.encolar_prioritario(2)
cola_prioridad.encolar(6)
cola_prioridad.encolar_prioritario(5)
cola_prioridad.encolar_prioritario(1)

while not cola_prioridad.esta_vacia():
	print('Desencolado: ', cola_prioridad.desencolar())
    
"""Observación : Los métodos de cola desencolar y ver_primero suelen lanzar una excepción si la misma está vacía. Acá en
nuestra ColaConPrioridad de forma implicita logramos ese mismo comportamiento al no manejar las excepciones cuando se
desencola o ve el primero de self.normales cuando dicha cola está vacía."""