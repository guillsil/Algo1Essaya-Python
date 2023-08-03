"""Implementar el método downsamp(k) para una implementación de ListaEnlazada con referencia úniccamente 
al primer nodo . Este método debe eliminar todo elemento de la lista que ocupe una posición que no sea
múltiple del npumero k pasado por parámetro (k > 1). Ejemplos:
l : [0, 1, 2, 3, 4, 5]                        -> l.downsamp(2) -> l : [0, 2, 4]
l : ["a", "b", "c", "d", "e", "f", "g"]       -> l.downsamp(4) -> l : ["a", "e"]
l : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]           -> l.downsamp(3) -> l : [1, 4, 7, 10]
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def agregar_elemento(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo

    def __str__(self):
        if self.primero is None:
            return "[]"

        actual = self.primero
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + " ".join(elementos) + "]"
    def downsamp(self, k):
        if k <= 1 or self.primero is None:
            return

        actual = self.primero
        anterior = None
        indice = 1

        while actual is not None:
            if indice > 1 and indice % k != 0:
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
            else:
                anterior = actual

            actual = actual.siguiente
            indice += 1
        


lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)
lista.agregar_elemento(5)

print(lista)
lista.downsamp(2)
print(lista)

"""Escribir una funcion recursiva que dada una cadena le haga un "flip" de mayúsculas, es decir, que devuelva 
una nueva cadena con los caracteres en mínuscula trasnformados a mayúscula y los carecteres en mayúscula 
transformados en minúscula"""
#iterativo
def intercambiar(cadena):
    nueva_cadena = ""
    for c in cadena:
        if c == c.lower():
            nueva_cadena += c.upper()
        else:
            nueva_cadena += c.lower()
    return nueva_cadena
cadena = "Hola"
print(intercambiar(cadena))

#recursivo

def intercambiar2(cadena, indice=0):
    nueva_cadena = ""
    if indice >= len(cadena):
        return nueva_cadena
    if cadena[indice].islower():
        nueva_cadena += cadena[indice].upper()
    else:
        nueva_cadena += cadena[indice].lower()
    nueva_cadena += intercambiar2(cadena, indice+1)
    return nueva_cadena

cadena = "Hola"
print(intercambiar2(cadena))

"""
A) Dada la lista [1,2,3,4,5,6,7,8,9,2], mostrar los pasos para ordenanrla mediante inserción y mergesort
B)Desarrolar en no as de 5 renglones , cual es el mejor entre esos dos métodos para lista dada y por que ?
"""











