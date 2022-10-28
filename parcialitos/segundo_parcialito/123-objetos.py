"""Implementar la clase Caramelera, que recibe en su constructor la cantidad de caramelos que puede contener,
y tiene el siguiente comportamiento:
#>>> c = Caramelera(20)            >>> c.sacar_caramelos(50)
#>>> c.poner_caramelos(10)        Traceback (most recent call last):
#>>> c.sacar_caramelos(4)         ...
#>>> c.caramelos()                ValueError: No quedan tantos caramelos!
6                                >>> c.poner_caramelos(50)
#>>> print(c)                     Traceback (most recent call last):
Caramelera con 6/20 caramelos    ...
                                    ValueError: No queda lugar para tantos caramelos
"""
class Caramelera:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cantidad = 0
    def poner_caramelos(self, cantidad):
        if self.cantidad + cantidad > self.capacidad:
            raise ValueError('No queda lugar para tantos caramelos')
        self.cantidad += cantidad
    def sacar_caramelos(self, cantidad):
        if self.cantidad - cantidad < 0:
            raise ValueError('No quedan tantos caramelos!')
        self.cantidad -= cantidad
    def caramelos(self):
        return self.cantidad
    def __str__(self):
        return 'Caramelera con {}/{} caramelos'.format(self.cantidad, self.capacidad)

