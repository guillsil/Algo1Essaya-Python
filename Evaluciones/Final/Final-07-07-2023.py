"""
Sea la clase ListaOrdenada, que permite almacenar elementos garantizando que siempre están ordenando .
Implementar los métodos :
.) __init__ , que crea una ListaOrdenada vacía 
.) agregar, que recibe un elemento y lo agrega a la lista , en tiempo lineal 
.) combinar , que recibe  otra ListaOrdenada y devuelve una nueva ListaOrdenada que contiene los elementos de 
ambas (dejenado las listas originales intactas), en tiempo lineal. 
"""
class Nodo:
    # Representa un nodo de la lista enlazada.
    # Recibe un dato y el nodo siguiente.
    def __init__(self, dato):
        self.dato = dato
        self.prox = None
 
class ListaOrdenada:
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

    def combinar(self, otra_lista):
        """Ordena los elementos de ambas listas y los combina en una nueva lista ordenada."""
        nueva_lista = ListaOrdenada()
        actual = self.prim
        actual_otra = otra_lista.prim
        while actual is not None and actual_otra is not None:
            if actual.dato < actual_otra.dato:
                nueva_lista.agregar(actual.dato)
                actual = actual.prox
            else:
                nueva_lista.agregar(actual_otra.dato)
                actual_otra = actual_otra.prox
        while actual is not None:
            nueva_lista.agregar(actual.dato)
            actual = actual.prox
        while actual_otra is not None:
            nueva_lista.agregar(actual_otra.dato)
            actual_otra = actual_otra.prox

        return nueva_lista

lista1 = ListaOrdenada()
lista1.agregar(1)
lista1.agregar(3)
lista1.agregar(5)
print(lista1)
lista2 = ListaOrdenada()
lista2.agregar(2)
lista2.agregar(4)
lista2.agregar(6)
print(lista2)
print(lista1.combinar(lista2))


"""
2) Escribir una funcion que recibe una lista de denominadores de billetes D y un precio p, y devuelve un diccionario
denominacion :n indicando cuantos billetes se necesitan de cada denominacion para cubrir el precio
p(de forma tal de utilizar la menor cantidad de billetes posible).
Asumir que la lista D esta ordenada de menor a mayor y no tiene elemetos duplicados. El algoritmo a 
implementar debe tomar la mayor cantidad posible de la primera denominacion luego la mayor cantidad posible de
la segunda, etc, hasta cubrir el precio p.
En caso de no poder cubrir exatamente   el precio p el algoritmo indicado , lanzar una excepción:
Ejemplo:
billetes([1000, 200, 100, 20, 10, 1], 458) -> {200:2, 20:2, 10:1, 1:8}
billetes([1000, 200, 100, 20, 10, 5], 458) -> Error
"""

def billetes(lista, precio):
    diccionario = {}
    for denominacion in lista:
        cantidad = precio // denominacion
        if cantidad > 0:
            diccionario[denominacion] = cantidad
            precio -= denominacion * cantidad
        
    if precio > 0:
        raise Exception("No se puede cubrir el precio exacto.")
    return diccionario

#print(billetes([1000, 200, 100, 20, 10, 1], 458))
#print(billetes([1000, 200, 100, 20, 10, 5], 458))

"""
3)Dada una Pila que contiene enteros , escribir una funcion que mueva los elementos pares de la pila hacia el 
tope y los elementos impares al fondo, manteniendo el orden relativo de cada conjunto.
Como estructuras auxiliares únicamente se permite usar pilas y /o colas.
"""
from pila import Pila
from cola import Cola

def mover_pares(pila):
    pilas_pares = Pila()
    pilas_impares = Pila()
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento % 2 == 0:
            pilas_pares.apilar(elemento)
        else:
            pilas_impares.apilar(elemento)
    while not pilas_impares.esta_vacia():
        pila.apilar(pilas_impares.desapilar())
    while not pilas_pares.esta_vacia():
        pila.apilar(pilas_pares.desapilar())

#Prueba
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)
#print(pila)
#mover_pares(pila)
#print(pila)

""""
4)Escribir un método de ListaEnlazadas que elimina los elementos duplicados contiguos . Ejemplo:
>>> l = ListaEnlazada([5, 2, 2, 2, 3, 8, 3, 2, 5, 5])
>>> l.eliminar_duplicados_contiguos()
>>> l
ListaEnlazada(5, 2, 3, 8, 3, 2, 5)
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

    def eliminar_dupliados_contiguos(self):
        if self.primero is None:
            raise Exception("Lista Vacia")

        actual = self.primero

        while actual.siguiente is not None:
            if actual.dato == actual.siguiente.dato:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

#Prueba
lista = ListaEnlazada()
lista.agregar_elemento(5)
lista.agregar_elemento(2)
lista.agregar_elemento(2)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(8)
lista.agregar_elemento(3)
lista.agregar_elemento(2)
lista.agregar_elemento(5)
lista.agregar_elemento(5)
#print(lista)
#lista.eliminar_dupliados_contiguos()
#print(lista)


"""5). Un producto es apto celiacos si no contiene TACC, es decir que uo contiene trigo. avena,
cebada ni Centeno.
Un supermercado tiene una base de datos de productos almacenada en un archivo CSV con el 
formato : id;nombre;ingredientes
Por ejemplo, una línea del archivo podria
1234; Choclo amarillo entero 350g;Granos de choclo, agua, sal, acido citrico, acido ascorbico

Escribir la función separar(entrada, con_tacc, sin_tacc) que recibe la ruta del archivo CSV
de entrada y dos rutas de solida. La función debe clasificar los productos según si tienen o no
TAC.C, y escribir en uno u otro archivo según el caso. Los archivos de salida debeti quedar con
el mismo formato que el de entrada"""

import csv

def separar(ruta_archivo, con_tacc, sin_tacc):
    with open(ruta_archivo, "r") as archivo:
        archivo_reader = csv.reader(archivo)
        with open(con_tacc, "w") as archivo_con_tacc, open(sin_tacc, "w") as archivo_sin_tacc:
            archivo_con_tacc_writer = csv.writer(archivo_con_tacc)
            archivo_sin_tacc_writer = csv.writer(archivo_sin_tacc)
            for linea in archivo_reader:
                if "trigo" in linea[2].lower() or "avena" in linea[2].lower() or "cebada" in linea[2].lower() or "centeno" in linea[2].lower():
                    archivo_con_tacc_writer.writerow(linea)
                else:
                    archivo_sin_tacc_writer.writerow(linea)


#Prueba
separar("productos.csv", "con_tacc.csv", "sin_tacc.csv")











