"""1. Implementar la función mezcla_de_preguntas(preguntas_categoria, orden) que recibe un diccionario con N "mazos" de categorías con preguntas para el Preguntados (cada mazo está representado como Pila), y que debe retornar una nueva Pila con todas las
preguntas. alternando 1 pregunta de cada categoría según el orden dado por eI parámetro orden. Las preguntas en el tope de cada mazo deben quedar en eI tope de la Pila resultante. La función debe vaciar todas las pilas del diccionario.
Se puede asumir que todos los mazos tienen la misma cantidad de preguntas, y que las categorias de orden coinciden con las claves del
diccionario preguntas_categoria. Ejemplo, donde a modo ilustrativo, eI primer elemento de cada pila vendría a ser eI elemento
del tope:
preguntas_categona = { "Ciencia": Pila( [CI, C2, C3)), Pila([DI, D2, D3]) }
pila_preguntas (preguntas _ categoria, ["Deportes", "Ciencia"] )
pila _ preguntas . desapilar() "DI:¿Cuánto plata adeuda Independiente?"
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
Dada una clase ListaEnIazada, la cuál solo cuenta con una referencia al primer nodo, escribir eI método nplicar(x, N) que modifica la lista enlazada de tal forma que los elementos igual a x de la misma se ven duplicados N veces. Se puede asumir que N
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
contar_descendientes (persona: Persona) -> int que cuente cuántos descendientes tiene dicha persona (es decir. hijos + nietos + bisnietcs + etc), utilizando recursión."""





