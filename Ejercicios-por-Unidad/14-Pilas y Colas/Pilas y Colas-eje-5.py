"""Crear una clase PilaConMaximo que soporte las operaciones de Pila
(apilar(elemento) y desapilar()), y además incluya el método obtener_maximo() en tiem-
po constante. Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los
máximos."""
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

print(p.obtener_maximo())