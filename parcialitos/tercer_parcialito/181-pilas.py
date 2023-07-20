"""Se cuenta con una clase FichaDeHanoi que tiene un método obtener_tamaño() que devuelve un entero que representa el tamaño de la ficha. Se cuenta con una clase Pila ya implementada. Implementar una clase TorreDeHanoi que cumpla con los siguientes metodos:

    colocarFicha que coloca una ficha en la torre. Solo se puede colocar una ficha en el tope si la torre está vacía, o la ficha es menor a la que está en el tope
    sacarFicha que devuelve una ficha de la torre. Solo se puede sacar de la torre la ficha más pequeña de la misma.

"""
class Pila:
    def __init__(self):
        self.items = []
    def estaVacia(self):
        return len(self.items) == 0
    def apilar(self, x):
        self.items.append(x)
    def desapilar(self):
        if self.estaVacia():
            raise Exception("La pila está vacía")
        return self.items.pop()
    def verTope(self):
        if self.estaVacia():
            raise Exception("La pila está vacía")
        return self.items[-1]
    def __str__(self):
        return str(self.items)
    
class FichaDeHanoi:
    def __init__(self, tamaño):
        self.tamaño = tamaño
    def obtener_tamaño(self):
        return self.tamaño
    
class TorreDeHanoi:
    def __init__(self):
        self.pila = Pila()

    def colocarFicha(self, ficha):
        if self.pila.estaVacia() or ficha.obtener_tamaño() < self.pila.verTope().obtener_tamaño():
            self.pila.apilar(ficha)
        else:
            raise Exception("No se puede colocar la ficha")
        
    def sacarFicha(self):
        if self.pila.estaVacia():
            raise Exception("La torre está vacía")
        return self.pila.desapilar()

torre = TorreDeHanoi()
torre.colocarFicha(FichaDeHanoi(3))
torre.colocarFicha(FichaDeHanoi(2))
torre.colocarFicha(FichaDeHanoi(1))
print(torre.sacarFicha().obtener_tamaño())
print(torre.sacarFicha().obtener_tamaño())
print(torre.sacarFicha().obtener_tamaño())
