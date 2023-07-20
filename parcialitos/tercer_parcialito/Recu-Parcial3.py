"""Implementar un método para una implementacion de ListaEnlazada con referencia únicamente al primer nodo que devuelve
una nueva lista enlazada compuesta por los elementos que se encuentran en las posiciones impares de la original.
Por ejemplo, para L = [3, 1, 6, 8, 9] el método debe devolver [1, 8].
"""
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
class ListaEnlazada:
    def __init__(self):
        self.primero = None
    def __str__(self):
        actual = self.primero
        lista = []
        while actual != None:
            lista.append(str(actual.dato))
            actual = actual.prox
        return f"Lista Enlazada({', '.join(lista)})"
    def impares(self):
        """Devuelve una nueva lista enlazada compuesta por los elementos que se encuentran en las posiciones impares de la original"""
        #no se pueden usar metodos de la lista
        if self.primero is None:
            return ListaEnlazada()
        actual = self.primero
        len = 0
        while actual is not None:
            len += 1
            actual = actual.prox
        if len == 1:
            return ListaEnlazada()
        actual = self.primero
        nueva = ListaEnlazada()
        for i in range(len):
            if i % 2 != 0 and i / i == 1:
                if nueva.primero is None:
                    nueva.primero = _Nodo(actual.dato)
                    actual = actual.prox
                    continue
                actual_nueva = nueva.primero
                while actual_nueva.prox is not None:
                    actual_nueva = actual_nueva.prox
                actual_nueva.prox = _Nodo(actual.dato)
            actual = actual.prox
        return nueva


#Probar
li = ListaEnlazada()
li.primero = _Nodo("3")
li.primero.prox = _Nodo("1")
li.primero.prox.prox = _Nodo("6")
li.primero.prox.prox.prox = _Nodo("8")
li.primero.prox.prox.prox.prox = _Nodo("9")
print(li)
print(li.impares())

"""Implementar una funcion recursiva que dada una cadena devuelva la cantidad de veces que aparece el primer caracter 
(sin contar la primera aparicion), en las posiciones pares de la cadena.Por ejemplo:
*) Para "No es tan fácil, que todo te salga bien" debe devolver 2.
*) Para "No es tan fácil que todo te salga bien" debe devolver 1.
"""
def contar(cadena):
    if len(cadena) == 0:
        return 0
    if len(cadena) == 1:
        return 0
    if len(cadena) == 2:
        if cadena[0] == cadena[1]:
            return 1
        else:
            return 0
    if cadena[0] == cadena[2]:
        return 1 + contar(cadena[1:])
    else:
        return contar(cadena[1:])
#Probar
print(contar("No es tan fácil, que todo te salga bien"))
print(contar("No es tan fácil que todo te salga bien"))

"""Dada la lista [1, 2, 4, 5, 6, 3, 7, 8] escribir el seguimiento del algoritmo de ordenamiento por merge sort. 
¿Cual es la complejidad temporal del algoritmo en este arreglo? ¿hay algun otro algoritmo de ordenamiento que tenga
 una complejidad menor en este caso menor para este caso. Justificar."""
def merge(izq, der):
    i = 0
    j = 0
    resultado = []
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado += izq[i:]
    resultado += der[j:]
    return resultado

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

print(merge_sort([1, 2, 4, 5, 6, 3, 7, 8]))


