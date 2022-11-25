"""Crear una clase PilaConMaximo que soporte las operaciones de Pila (apilar(elemento), desapilar() y
ver_tope()), y además incluya el método obtener_maximo() en tiempo constante.
>> p = PilaConMaximo()
>> p.apilar(3)
>> p.obtener_maximo()
>> p.apilar(6)
>> p.obtener_maximo()
>> p.ver_tope()
>> p.apilar(2)
>> p.obtener_maximo()
>> p.ver_tope()
>> p.desapilar()
>> p.desapilar()
>> p.obtener_maximo()
Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los máximos.
Nota: Se encuentran disponibles los TDA Pila y Cola con sus métodos ya definidos en los archivos pila.py y
cola.py respectivamente."""
from pila import Pila
from cola import Cola
class PilaConMaximo:
    def __init__(self):
        self.pila = []
        self.maximos = []
    def apilar(self, elemento):
        self.pila.append(elemento)
        if len(self.maximos) == 0 or elemento >= self.maximos[-1]:
            self.maximos.append(elemento)
    def desapilar(self):
        elemento = self.pila.pop()
        if elemento == self.maximos[-1]:
            self.maximos.pop()
        return elemento
    def obtener_maximo(self):
        return self.maximos[-1]
#probar
p = PilaConMaximo()
p.apilar(1)
p.apilar(2)
p.apilar(3)
p.apilar(100)

print(p.obtener_maximo())