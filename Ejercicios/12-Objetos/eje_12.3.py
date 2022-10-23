"""a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
misma cantidad de elementos debe levantar una excepción.
c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con
los elementos multiplicados por ese número."""
#a)
class Vector:
    def __init__(self, lista):
        self.lista = lista
    def __str__(self):
        return f"{self.lista}"
    #b)
    def __add__(self, otro):
        if len(self.lista) != len(otro.lista):
            raise ValueError("No se pueden sumar")
        else:
            for i in range(len(self.lista)):
                self.lista[i] += otro.lista[i]
            return Vector(self.lista)
    #c)
    def __mul__(self, numero):
        for i in range(len(self.lista)):
            self.lista[i] *= numero
        return Vector(self.lista)


"""probar el objeto"""
vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])
print(vector1.__str__())
print(vector1.__add__(vector2))
print(vector2.__mul__(2))

