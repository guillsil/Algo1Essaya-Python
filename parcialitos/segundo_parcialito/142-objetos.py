"""Se pide crear una clase Auto que actue de la siguiente forma:

>>> auto = Auto('rojo', ‘gol’)      >>> auto.avanzar(5)
>>> auto.avanzar(5)                 >>> auto.avanzar(6)
ValueError: No hay suficiente       ValueError: No hay suficiente
combustible.                        combustible.
>>> auto.cargaCombustible(10)       >>> print(auto)
                                    Auto de color rojo, modelo gol, 5L de combustible

Comentario: Para simplificar las cuentas, lo que se carga de combustible es equivalente a lo que se gasta para avanzar. Por lo tanto si avanza 5Km, gasta entonces 5l de combustible. De no tener el combustible para avanzar lo indicado, no avanza y levanta una excepción.
"""
class Auto:
    def __init__(self, color, modelo):
        self.color = color
        self.modelo = modelo
        self.combustible = 0
    def avanzar(self, pasos):
        if self.combustible < pasos:
            raise ValueError("No hay suficiente combustible")
        else:
            self.combustible -= pasos
    def cargaCombustible(self, cantidad):
        self.combustible += cantidad
    def __str__(self):
        return f"Auto de color {self.color}, modelo {self.modelo}, {self.combustible}L de combustible"
    
auto = Auto('rojo', 'gol')
auto.avanzar(5)
auto.avanzar(5)
auto.cargaCombustible(10)
print(auto)
auto.avanzar(5)
auto.avanzar(6)
print(auto)
