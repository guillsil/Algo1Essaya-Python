"""Se quiere modelar un perchero para colgar ropa. Se pide crear las clases Perchero y Prenda tal que se
se puedan ejecutar las siguientes líneas de código y se obtengan los resultados especificados.
El constructor de Perchero recibe la cantidad de espacio total disponible, y el de Prenda recibe
el nombre de la prenda y cuánto espacio ocupa:
>>> p = Perchero(3)
>>> p.colgar(Prenda('camisa', 1))
>>> p.colgar(Prenda('pantalon', 1))
>>> p.sacar('pantalon')
Prenda('pantalon', 1)
>>> p.sacar('remera')
Exception: No se encontró la prenda
>>> p.espacio_disponible()
2
>>> p.colgar(Prenda('campera', 3))
Exception: No hay espacio para colgar la prenda
"""
class Perchero:
    def __init__(self, espacio_total):
        self.espacio_total = espacio_total
        self.espacio_disponible = espacio_total
        self.prendas = []
    def colgar(self, prenda):
        if prenda.espacio > self.espacio_disponible:
            raise Exception('No hay espacio para colgar la prenda')
        self.prendas.append(prenda)
        self.espacio_disponible -= prenda.espacio
    def sacar(self, nombre):
        for prenda in self.prendas:
            if prenda.nombre == nombre:
                self.prendas.remove(prenda)
                self.espacio_disponible += prenda.espacio
                return prenda
        raise Exception('No se encontró la prenda')
    def espacio_disponible(self):
        return self.espacio_disponible
class Prenda:
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio
    def __str__(self):
        return 'Prenda({}, {})'.format(self.nombre, self.espacio)