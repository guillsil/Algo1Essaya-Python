"""1. Implementar la función mezcla_de_preguntas(preguntas_categoria, orden) que recibe un diccionario con N "mazos" de
categorías con preguntas para el Preguntados (cada mazo está representado como Pila), y que debe retornar una nueva Pila
con todas las
preguntas. alternando 1 pregunta de cada categoría según el orden dado por eI parámetro orden. Las preguntas en el tope de
 cada mazo deben quedar en eI tope de la Pila resultante. La función debe vaciar todas las pilas del diccionario.
Se puede asumir que todos los mazos tienen la misma cantidad de preguntas, y que las categorias de orden coinciden con
 las claves del
diccionario preguntas_categoria. Ejemplo, donde a modo ilustrativo, eI primer elemento de cada pila vendría a ser eI elemento
del tope:
preguntas_categona = { "Ciencia": Pila( [CI, C2, C3)), Pila([DI, D2, D3]) }
pila_preguntas (preguntas _ categoria, ["Deportes", "Ciencia"] )
pila _ preguntas . 1. Implementar la función mezcla_de_preguntas(preguntas_categoria, orden) que recibe un diccionario con N "mazos" de
categorías con preguntas para el Preguntados (cada mazo está representado como Pila), y que debe retornar una nueva Pila
con todas las
preguntas. alternando 1 pregunta de cada categoría según el orden dado por eI parámetro orden. Las preguntas en el tope de
 cada mazo deben quedar en eI tope de la Pila resultante. La función debe vaciar todas las pilas del diccionario.
Se puede asumir que todos los mazos tienen la misma cantidad de preguntas, y que las categorias de orden coinciden con
 las claves del
diccionario preguntas_categoria. Ejemplo, donde a modo ilustrativo, eI primer elemento de cada pila vendría a ser eI elemento
del tope:
preguntas_categona = { "Ciencia": Pila( [CI, C2, C3)), Pila([DI, D2, D3]) }
pila_preguntas (preguntas _ categoria, ["Deportes", "Ciencia"] )
pila _ preguntas . desapilar() "DI:¿Cuánto plata adeuda Independiente?"
pila _ preguntas . desapilar() "CI: ¿Quién inventó eI Cálculo Lambda?"

pila_preguntas. desapilar() "D2: ¿Cuántas UEFA CL tiene eI Inter Milán?"
pila_preguntas. desapilar():
 desapilar() # >> "C2: ¿Cuál es eI número atómico del Neón?desapilar() "DI:¿Cuánto plata adeuda Independiente?"
pila _ preguntas . desapilar() "CI: ¿Quién inventó eI Cálculo Lambda?"

pila_preguntas. desapilar() "D2: ¿Cuántas UEFA CL tiene eI Inter Milán?"
pila_preguntas. desapilar():
 desapilar() # >> "C2: ¿Cuál es eI número atómico del Neón?"
"""
from pila import Pila
from cola import Cola

def mezcla_de_preguntas(preguntas_categoria, orden):
    preguntas = Pila()
    for i in range(len(orden)):
        categoria = preguntas_categoria[orden[i]]
        while not categoria.esta_vacia():
            preguntas.apilar(categoria.desapilar())
    return preguntas

    
ciencia = Pila()
ciencia.apilar("¿Quién inventó el Cálculo Lambda?")
ciencia.apilar("¿Cuál es el número atómico del Neón?")
ciencia.apilar("¿Cuánto es 2 + 2?")

deportes = Pila()
deportes.apilar("¿Cuántas UEFA CL tiene el Inter Milán?")
deportes.apilar("¿Cuánto plata adeuda Independiente?")
deportes.apilar("¿Cuántos mundiales ganó Argentina?")

preguntas_categoria = { "Ciencia": ciencia, "Deportes": deportes}
pila_pregunta = mezcla_de_preguntas(preguntas_categoria, ["Deportes", "Ciencia"])
print(pila_pregunta.desapilar())
print(pila_pregunta.desapilar())
print(pila_pregunta.desapilar())
print(pila_pregunta.desapilar())
print(pila_pregunta.desapilar())
print(pila_pregunta.desapilar())

"""#2 
Dada una clase ListaEnIazada, la cuál solo cuenta con una referencia al primer nodo, escribir eI método nplicar(x, N) 
que modifica la lista enlazada de tal forma que los elementos igual a x de la misma se ven duplicados N veces. Se puede asumir que N
mayor a cero. EI método no debe iterar la lista más de una vez. Ejemplos de cómo quedaría la lista antes y después de llamar al metodo.
l = 6 -> 8 -> 6 -> 5 -> 5
l.aplicar(6, 3) # l = 6 -> 6 -> 6 -> 8 -> 6 -> 6 -> 6 -> 5 -> 5 -> 5 -> 5 -> 5
l.aplicar(5, 2) # l = 6 -> 6 -> 6 -> 8 -> 6 -> 6 -> 6 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5
l.aplicar(6,1) # l = 6 -> 6 -> 6 -> 8 -> 6 -> 6 -> 6 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5
l.aplicar(9, 2) # l = 6 -> 6 -> 6 -> 8 -> 6 -> 6 -> 6 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5
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
    def napilar(self, x , n):
        if self.primero is None:
            raise Exception("Lista vacia")
        actual = self.primero
        while actual is not None:
            if actual.dato == x:
                for i in range(n-1):
                    nodo = Nodo(x)
                    nodo.siguiente = actual.siguiente
                    actual.siguiente = nodo
                    actual = actual.siguiente
            actual = actual.siguiente

    def napilar2(self, x, n):
        if self.primero is None:
            raise Exception("lista Vacia")
        actual = self.primero
        while actual is not None:
            if actual.dato == x:
                for i in range(n)-1:
                    nodo = Nodo(x, actual.siguiente)
                    actual.siguiente = nodo
                    actual = actual.siguiente
            actual = actual.siguiente






        
l = ListaEnlazada()
l.agregar_elemento(6)
l.agregar_elemento(8)
l.agregar_elemento(6)
l.agregar_elemento(5)
l.agregar_elemento(5)
print(l)
l.napilar(6, 3)
print(l)

"""#3
Existiendo la clase Persona, que posee el método  obtener_hijos() -> List [Persona], se pide implementar una función
contar_descendientes (persona: Persona) -> int que cuente cuántos descendientes tiene dicha persona 
(es decir. hijos + nietos + bisnietcs + etc), utilizando recursión."""

class Persona:
    def __init__(self, nombre, hijos):
        self.nombre = nombre
        self.hijos = hijos

    def obtener_hijos(self):
        return self.hijos

    def contar_descendientes(self, persona):
        if self.obtener_hijos() == []:
            return 0
        else:
            total_descendiente = 0
            for hijo in self.obtener_hijos():
                total_descendiente += 1 + hijo.contar_descendientes(hijo)

        return total_descendiente

p1 = Persona("Juan", [])
p2 = Persona("Pedro", [])
p3 = Persona("Ana", [p1, p2])
p4 = Persona("Maria", [p3])
print(p4.contar_descendientes(p4))

#Extras de recursion
"""Implementar una función buscar_elemento que reciba una lista enlazada y un elemento como parámetros y
devuelva True si el elemento se encuentra en la lista, o False en caso contrario.
La función debe utilizar recursión para recorrer la lista enlazada."""
#iterativo
def buscar_elemento(lista_enlazada, elemento):
    actual = lista_enlazada.primero
    while actual is not None:
        if actual.dato == elemento:
            return True
        actual = actual.siguiente
    return False
#recursivo
def buscar_elemento2(lista_enlazada, elemento):
    actual = lista_enlazada.primero
    if actual is None:
        return False
    if actual.dato == elemento:
        return True
    nueva_lista = ListaEnlazada
    nueva_lista.primero = actual.siguiente
    return buscar_elemento2(nueva_lista, elemento)


lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)

print(buscar_elemento(lista, 3))
print(buscar_elemento2(lista, 6))

"""Escribir una función eliminar_duplicados que reciba una lista enlazada como parámetro y elimine todos
los elementos duplicados, dejando únicamente el primer elemento de cada valor repetido. 
Por ejemplo, si la lista es 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 4, la función debe modificar la lista a 1 -> 2 -> 3 -> 4."""
#iterativo
def eliminar_duplicados(lista_enlazada):
    actual = lista_enlazada.primero
    while actual is not None:
        if actual.siguiente is not None and actual.dato == actual.siguiente.dato:
            actual.siguiente = actual.siguiente.siguiente
        else:
            actual = actual.siguiente

#recursivo
def eliminar_duplicados2(lista_enlazada):
    actual = lista_enlazada.primero
    if actual is None:
        return
    if actual.siguiente is not None and actual.dato == actual.siguiente.dato:
        actual.siguiente = actual.siguiente.siguiente
        nueva_lista = ListaEnlazada()
        nueva_lista.primero = actual
        eliminar_duplicados2(nueva_lista)
    else:
        nueva_lista = ListaEnlazada()
        nueva_lista.primero = actual.siguiente
        eliminar_duplicados2(nueva_lista)

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(3)

eliminar_duplicados(lista)
print(lista)


"""Implementar una función invertir_lista que reciba una lista enlazada y la invierta utilizando recursión. 
Por ejemplo, si la lista es 1 -> 2 -> 3 -> 4, la función debe modificarla a 4 -> 3 -> 2 -> 1."""
#iterativo
def invertir_lista(lista_enlazada):
    actual = lista_enlazada.primero
    anterior = None
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        actual, anterior = siguiente, actual
    lista_enlazada.primero = anterior

#recursivo
def invertir_lista(lista_enlazada):
    actual = lista_enlazada.primero
    pila = Pila()
    while actual is not None:
        pila.apilar(actual.dato)
        actual = actual.siguiente
    actual = lista_enlazada.primero
    while not pila.esta_vacia():
        actual.dato = pila.desapilar()
        actual = actual.siguiente



lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)
print(lista)
invertir_lista(lista)
print(lista)

"""Escribir una función sumar_elementos que reciba una lista enlazada que contiene enteros y devuelva la 
suma de todos los elementos utilizando recursión."""

#iterativo
def sumar_elementos(lista_enlazada):
    actual = lista_enlazada.primero
    suma = 0
    while actual is not None:
        suma += actual.dato
        actual = actual.siguiente
    return suma
#recursivo
def sumar_elementos2(lista_enlazada):
    actual = lista_enlazada.primero
    if actual is None:
        return 0
    nueva_lista = ListaEnlazada()
    nueva_lista.primero = actual.siguiente
    return actual.dato + sumar_elementos2(nueva_lista)

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)

print(sumar_elementos(lista))
print(sumar_elementos2(lista))

"""Crear una función contar_nodos que cuente la cantidad de nodos en una lista enlazada utilizando recursión.

Recuerda que para implementar estos ejercicios, necesitarás tener definida una clase para la lista enlazada y sus métodos,
como __init__, agregar, obtener_siguiente, entre otros. Además, es importante manejar los casos base correctamente para 
evitar bucles infinitos en las funciones recursivas. ¡Espero que estos ejercicios te sean útiles para practicar y afianzar 
tus habilidades con listas enlazadas y recursión!
"""
#iterativo
def contar_nodos(lista_enlazada):
    actual = lista_enlazada.primero
    contador = 0
    while actual is not None:
        contador += 1
        actual = actual.siguiente
    return contador
#recursivo
def contar_nodos2(lista_enlazada):
    actual = lista_enlazada.primero
    if actual is None:
        return 0
    nueva_lista = ListaEnlazada()
    nueva_lista.primero = actual.siguiente
    return 1 + contar_nodos2(nueva_lista)

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)










