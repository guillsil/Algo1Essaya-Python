"""
a)
Implementar la clase TrianguloRectangulo, con los siguientes métodos:
• init que crea un triángulo rectángulo a partir de la longitud de sus catetos
Debe lanzar una excepción si alguno de los catetos es negativo.
• perimetro que calcula el perímetro del triángulo.
• area que calcula el área del triángulo.
b)
Implementar el o los metodos necesarios para que al ordenar una lista de triangulos , se ordene
automaticamente por sus respectivas areas. Es decir , para que el siguienete ejemplo funcione:
>> tris = [
TrianguloRectangulo(3, 4),
TrianguloRectangulo(1, 2),
TrianguloRectangulo(5, 6),]
>> tris.sort() # Ordena por area
>> tris # Muestra el resultado
[TrianguloRectangulo(1, 2), TrianguloRectangulo(3, 4), TrianguloRectangulo(5, 6)]
Recordatorio: un tríangulo rectángulo tiene dos catetos (a, b) y una hipotenusa (c) que se calcula  como c = √a2 + b2
"""
class TrianguloRectangulo:
    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("Los catetos no pueden ser negativos")
        #si self es una instancia de la clase TrianguloRectangulo
        self.a = a
        self.b = b
        self.c = (a**2 + b**2)**0.5

    def perimetro(self):
        return self.a + self.b + self.c

    def  area(self):
        return self.a * self.b / 2

    def __repr__(self):
        return f"TrianguloRectangulo({self.a}, {self.b})"


class Triangulos:
    def __init__(self, lista):
        self.lista = lista

    def __repr__(self):
        return f"Triangulos({self.lista})"

    def sort(self):
        self.lista.sort(key=lambda x: x.area())
        return self.lista


tri1 = TrianguloRectangulo(3, 4)
tri2 = TrianguloRectangulo(1, 2)
tri3 = TrianguloRectangulo(5, 6)

tris = Triangulos([tri1, tri2, tri3])
print(tris.sort())

"""
Escribir una funcion que reciba un número entero n , y devuevlava una matriz triangular superior de dimension n x n,
en forma de lista de listas , cuyos elementos no nulos son los números naturales en orden .
Por ejemplo: para n = 4 , debe devolver la siguiente matriz:
[[1, 2, 3, 4],
[0, 5, 6, 7],
[0, 0, 8, 9],
[0, 0, 0, 10]]
"""
def matriz_singular(n):
    matriz = []
    fila = []
    k = 1
    d = 0
    for i in range(n):
        for j in range(n):
            if j >= d:
                fila.append(k)
                k += 1
            else:
                fila.append(0)
        matriz.append(fila)
        fila = []
        d += 1
    return matriz
print(matriz_singular(4))

"""
Escribir en forma recursiva la función filtrar(cola, f) que recibe una cola y una funcion , y devuelve una nueva cola 
que contiene los elemenetos para los cuales los elementos de f devuelve True. La cola recibida debe quedar 
vacía al finalizar la ejecucion . Ejemplo:
>>> filtrar(Cola([1, 2, 3, 4, 5]), es_par) -> Cola([2, 4])
"""
#Iterativo
from cola import Cola
def filtrar(cola, f):
    cola_nueva = Cola()
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if f(dato):
            cola_nueva.encolar(dato)
    return cola_nueva

#Recursivo
def filtrar2(cola, f):
    if cola.esta_vacia():
        return cola
    dato = cola.desencolar()
    cola_filtrada = filtrar2(cola, f)
    if f(dato):
        cola_filtrada.encolar(dato)
    return cola_filtrada


cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)
print(filtrar2(cola, lambda x: x % 2 == 0))


"""
Implementar el método de ListaEnlazada partir(n) que devuelve una nueva ListaEnlazada , de forma tal que la lista original 
quede con sus primeros n elementos , y la lista nueva con los elementos restantes . Ejemplo:
>>> lista = ListaEnlazada([1, 2, 3, 4, 5])
>>> lista2 = lista.partir(3)    
>>> lista
ListaEnlazada([1, 2, 3])    
>>> lista2
ListaEnlazada([4, 5])
"""
class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0

    def __str__(self):
        actual = self.prim
        lista = []
        while actual:
            lista.append(str(actual.dato))
            actual = actual.prox
        return " ".join(lista)

    def agregar(self, dato):
        nodo = Nodo(dato)
        if not self.prim:
            self.prim = nodo
        else:
            actual = self.prim
            while actual.prox:
                actual = actual.prox
            actual.prox = nodo
        self.len += 1





