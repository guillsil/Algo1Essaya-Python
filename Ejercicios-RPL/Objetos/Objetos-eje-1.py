"""Este ejercicio está resuelto en el apunte teórico de la materia, bajo la sección 14.3 Definiendo nuevos tipos.
Escribir una clase para representar un punto en dos dimensiones. La clase debe tener los siguientes métodos:
    Un constructor que reciba sus dos coordenadas y las asigne a los atributos x e y del objeto (para los fines de este ejercicio, no hace falta validar que estos sean números).
    distancia(otro): devuelve la distancia entre el mismo punto y otro.
    restar(otro): devuelve un punto que resulta de la resta entre el mismo punto y otro.
    norma(): devuelve la norma del vector dado por el punto.
Ejemplo de ejecución:
#>>> p = Punto(5, 7)
#>>> q = Punto(2, 3)
#>>> r = p.restar(q)
#>>> (r.x, r.y)
(3, 4)
#>>> r.norma()
5.0
#>>> q.distancia(r)
1.41421356237"""
import math

class Punto:
    """
    Representación de un punto en el plano en
    coordenadas cartesianas (x, y)
    """

    def __init__(self, x, y):
        """
        Constructor de Punto. x e y deben ser numéricos
        """
        self.x = x
        self.y = y

    def distancia(self, otro):
        """
        Devuelve la distancia entre ambos puntos.
        """
        return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)


    def restar(self, otro):
        """
        Devuelve el Punto que resulta de la resta
        entre dos puntos.
        """
        return Punto(self.x - otro.x, self.y - otro.y)
    def norma(self):
        """
        Devuelve la norma del punto.
        """
        return math.sqrt(self.x**2 + self.y**2)

