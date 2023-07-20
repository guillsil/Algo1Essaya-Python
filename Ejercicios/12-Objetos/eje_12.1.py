"""a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta.
b) Implementar el método duracion que devuelve la duración en segundos del intervalo.
c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo in-
tervalo resultante de la intersección entre ambos, o lanzar una excepción si la intersección
es nula.
d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adya-
centes ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
intervalo resultante de la unión entre ambos."""
#a)
class Intervalo:
    def __init__(self, desde, hasta):
        self.desde = desde
        self.hasta = hasta
        if self.desde > self.hasta:
            raise ValueError("El valor desde debe ser menor que el valor hasta")
    #b)
    def duracion(self):
        return self.hasta - self.desde
    #c)
    def interseccion(self, otro):
        if self.desde > otro.hasta or self.hasta < otro.desde:
            raise ValueError("No hay interseccion")
        else:
            return Intervalo(max(self.desde, otro.desde), min(self.hasta, otro.hasta))
    #d)
    def union(self, otro):
        if self.desde > otro.hasta or self.hasta < otro.desde:
            raise ValueError("No hay union")
        else:
            return Intervalo(min(self.desde, otro.desde), max(self.hasta, otro.hasta))
""""probar el objeto"""
intervalo1 = Intervalo(1, 10)
intervalo2 = Intervalo(5, 15)
intervalo3 = Intervalo(20, 30)
print(intervalo1.duracion())
print(intervalo1.interseccion(intervalo2).duracion())
print(intervalo1.union(intervalo2).duracion())
