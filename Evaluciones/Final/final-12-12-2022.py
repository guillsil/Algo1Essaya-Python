"""1. Representamos un intervalo de tiempo de la forma (a, b), siendo a el instante en el que
comienza el intervalo y b el instante en el que finaliza (a < b).
Escribir una función que reciba una lista de intervalos ordenados por el valor de a y devuelva
una lista en la que los intervalos superpuestos hayan sido combinados. Por ejemplo, los inter-
valos (1, 4) y (3, 5) se combinan obteniendo (1, 5). Si el fin y el inicio de dos intervalos son
exactamente iguales, se considera que son superpuestos.
Ejemplo: combinar_intervalos([(1,5), (2,3), (4,6), (7,8), (8,10), (12,15)]) ➡ [(1,6),(7,10), (12,15)]

Recomendación: pensar la función en forma recursiva.
"""
def combinar_intervalos(intervalos):
    """Recibe una lista de intervalos ordenados por el valor de a y devuelve una lista en la que los intervalos superpuestos hayan sido combinados."""
    if len(intervalos) == 1:
        return intervalos
    if intervalos[0][1] >= intervalos[1][0]:
        return combinar_intervalos([(intervalos[0][0], max(intervalos[0][1], intervalos[1][1]))] + intervalos[2:])
    else:
        return [intervalos[0]] + combinar_intervalos(intervalos[1:])

print(combinar_intervalos([(1,5), (2,3), (4,6), (7,8), (8,10), (12,15)]))


"""Se desea determinar si una contraseña que contiene únicamente letras minúsculas está formada
por una secuencia de palabras. Escribir la función es_palabras(contraseña, palabras), que
recibe la contraseña y una lista de palabras, y devuelve True si la contraseña se puede formar
concatenando las palabras en cualquier orden (posiblemente repitiendo palabras).
Por ejemplo, si la lista de palabras es ['agua', 'tierra', 'fuego', 'aire']:
es_palabras('agua', palabras) ➡ True es_palabras('auga', palabras) ➡ False
es_palabras('aguaaire', palabras) ➡ True es_palabras('aguaire', palabras) ➡ False
es_palabras('aguaagua', palabras) ➡ True
Recomendación: pensar la función en forma recursiva."""
palabras = ['agua', 'tierra', 'fuego', 'aire']
#iterativa
def es_palabras(contrasenia, palabras):
    """Determina si una contraseña que contiene únicamente letras minúsculas está formada por una secuencia de palabras."""

    for palabra in palabras:
        if palabra in contrasenia:
            contrasenia = contrasenia.replace(palabra, '')
    return contrasenia == ''

diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario.get("a", 0))

print(es_palabras('agua', palabras))
print(diccionario.keys())

#recursiva
def es_palabras(contrasenia, palabras):
    if contrasenia == "":
        return True
    
    for palabra in palabras:
        if palabra in contrasenia:
            return es_palabras(contrasenia.replace(palabra, ''), palabras)
    return False

    
    
print(es_palabras("aguaire", palabras))

"""El algoritmo de búsqueda por interpolación es una variación de búsqueda binaria. En cada paso,
en lugar de seleccionar el elemento que está en la mitad del arreglo, se hace una interpolación
lineal entre los elementos de los extremos.
Por ejemplo, si buscamos el número 𝑥 = 22 en un arreglo 𝐿 entre las posiciones 𝑖𝑧𝑞 = 0 y
𝑑𝑒𝑟 = 99, el primer paso sería inspeccionar los elementos de los extremos. Supongamos que
𝐿[𝑖𝑧𝑞] = 𝐿[0] = 15 y 𝐿[𝑑𝑒𝑟] = 𝐿[99] = 84; entonces, si los elementos están distribuidos en forma
uniforme, el número 22 debería estar más cerca del índice 0 que del índice 99. Así podemos
efectuar la interpolación:
𝑚𝑒𝑑 = 𝑖𝑧𝑞 + ⌊(𝑑𝑒𝑟 − 𝑖𝑧𝑞) 𝑥 − 𝐿[𝑖𝑧𝑞]
𝐿[𝑑𝑒𝑟] − 𝐿[𝑖𝑧𝑞] ⌋ = 0 + ⌊(99 − 0) 22 − 15
84 − 15 ⌋ = 10
El próximo paso será inspeccionar el elemento en 𝐿[𝑚𝑒𝑑] = 𝐿[10], continuando igual que en
búsqueda binaria.
Escribir una función que reciba una lista de números y un número a buscar, y devuelva el
índice del número o -1 si no está en la lista, utilizando búsqueda por interpolación."""
def busqueda_interpolacion(lista, numero):
    izq= 0
    der = len(lista) -1
    while izq <= der:
        med = izq + int(((der- izq)*((numero-lista[izq])/(lista[der]- lista[izq]))))
        if lista[med] == numero:
            return med
        elif lista[med] > numero:
            izq = med +1
        else:
            der = med -1
    return -1

print(busqueda_interpolacion([1,2,3,4,5,6,7,8,9,10], 5))

"""El sitio web imdb tiene una base de datos de películas almacenada en un archivo CSV con el
formato id;nombre;elenco. Por ejemplo, una línea del archivo podría ser:
1234;El Padrino;Marlon Brando,Al Pacino,James Caan
Escribir una función que reciba la ruta del archivo y el nombre de un actor y devuelva una
lista con los nombres de las películas en las que actúa el actor."""
import csv
def participaciones_en_peliculas(ruta_archivo, actor):
    with open(ruta_archivo, "r") as archivo:
        lista_de_peliculas = []
        diccionario = {}
        archivo_reader = csv.reader(archivo)
        for ids, nombre, elenco in archivo_reader:
            elenco = elenco.split(",")
            for personaje in elenco:
                if personaje not in diccionario:
                    diccionario[personaje] = [nombre]
                else:
                    diccionario[personaje].append(nombre)
        return diccionario.get(actor, [])
    
"""print(participaciones_en_peliculas("peliculas.csv", "Al Pacino"))"""

"""Suponiendo que ya existe la clase Nodo, implementar la clase Pila en la que cada elemento
se almacena en un nodo enlazado. Implementar los métodos __init__, apilar, desapilar,
ver_tope y esta_vacia"""

class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class Pila():
    def __init__(self):
        self.tope = None
        self.len = 0

    def apilar(self, dato):
        self.tope = Nodo(dato, self.tope)
        self.len += 1


    def esta_vacia(self):
        return self.tope is None

    def desapilar(self):
        if self.esta_vacia():
            raise ValueError("La pila está vacía")
        dato = self.tope.dato
        self.tope = self.tope.prox
        self.len -= 1
        return dato
    
    def ver_tope(self):
        if self.esta_vacia():
            raise ValueError("La pila está vacía")
        return self.tope.dato
    
    def __str__(self):
        actual = self.tope
        lista = []
        while actual is not None:
            lista.append(actual.dato)
            actual = actual.prox
        return str(lista)

    
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print(pila)
print(pila.ver_tope())

class Cola():
    def __init__(self):
        self.prim = None
        self.ultimo = None
        self.len = 0
    
    def encolar(self, dato):
        nodo = Nodo(dato)
        if self.esta_vacia():
            self.prim = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo
        self.len += 1

    def esta_vacia(self):
        return self.prim is None
    
    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        dato = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        if not self.prim:
            self.ultimo = None
        return dato
    
    def __str__(self)









