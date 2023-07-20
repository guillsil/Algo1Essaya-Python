"""Crear una clase Vector, que en su constructor reciba una lista de elementos que serán sus coordenadas.
En el método __str__ se imprime su contenido con el formato [x,y,z]. La cantidad de coordenadas que puede
manejar el vector debe ser dinámica: su constructor puede recibir una lista con un solo elemento o con N elementos.

La clase debe tener los siguientes métodos:

__add__ que recibe otro vector. Verifica si tienen la misma cantidad de elementos y devuelva un nuevo vector con
la suma de ambos. Si no tienen la misma cantidad de elementos debe levantar una excepción Exception: Vectores no tienen
la misma cantidad de elementos.

__mul__ que recibe un número y devuelve un nuevo vector, con los elementos multiplicados por ese número.
"""
class Vector:
    def __init__(self, lista):
        self.lista = lista
    def __str__(self):
        return str(self.lista)
    def __add__(self, v2):
        if len(self.lista) == len(v2.lista):
            lista = []
            for i in range(len(self.lista)):
                lista.append(self.lista[i] + v2.lista[i])
                return Vector(lista)
        else:
            raise Exception('Vectores no tienen la misma cantidad de elementos')
    def __mul__(self, n):
        lista = []
        for i in range(len(self.lista)):
            lista.append(self.lista[i] * n)
        return Vector(lista)


vector1 = Vector([1,2,3])
vector2 = Vector([4,5,6, 3])
vector3 = Vector([7,8,9])
print(vector1.__str__())
print(vector2.__add__(vector3))