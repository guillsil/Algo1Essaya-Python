"""a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.
b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
con la suma de ambas.
c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
con el producto de ambas.
d) Crear un método simplificar que modifica la fracción actual de forma que los valores
del dividendo y divisor sean los menores posibles."""
# a)
class Fraccion:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
    def __str__(self):
        return f"{self.dividendo}/{self.divisor}"
    # b)
    def __add__(self, otra):
        return Fraccion(self.dividendo * otra.divisor + self.divisor * otra.dividendo, self.divisor * otra.divisor)
    # c)
    def __mul__(self, otra):
        return Fraccion(self.dividendo * otra.dividendo, self.divisor * otra.divisor)
    # d)
    def simplificar(self):
        for i in range(2, min(self.dividendo, self.divisor) + 1):
            while self.dividendo % i == 0 and self.divisor % i == 0:
                self.dividendo //= i
                self.divisor //= i
"""probar el objeto"""
fraccion1 = Fraccion(4, 2)
fraccion2 = Fraccion(1, 4)
print(fraccion1 + fraccion2)
print(fraccion1 * fraccion2)
fraccion1.simplificar()
print(fraccion1)
