"""1. Cumpla las siguientes consignas para resolver el ejercicio, siguiendo el orden de a-b-c.
(3p)
a. Escribe una función llamada
group_movies_by_month_year que tome como entrada
un diccionario con las películas y sus fechas de estreno y devuelva otro diccionario que
agrupe las películas por mes y año. (1p)
b. Crea un diccionario de películas con fechas de estreno y prueba la función
group_movies_by_month_year con este diccionario. (1p)
c. Amplía la función
group_movies_by_month_year para que devuelva las películas
ordenadas alfabéticamente en la lista de cada mes y año
mivies = {
"Avatar": "2009-12-10",
"Titanic": "1997-11-18",
"Star Wars: Episode IV - A New Hope": "1977-05-25",
}
"""
#a
def group_movies_by_month_year(diccionario):
    diccionario_final = {}
    for pelicula, fecha in diccionario.items():
        fecha = fecha.split("-")
        if fecha[0] not in diccionario_final:
            diccionario_final[fecha[0]] = {}
        if fecha[1] not in diccionario_final[fecha[0]]:
            diccionario_final[fecha[0]][fecha[1]] = []
        diccionario_final[fecha[0]][fecha[1]].append(pelicula)
    return diccionario_final

#b
movies = {
"Avatar": "2009-12-10",
"Titanic": "1997-11-18",
"Star Wars: Episode IV - A New Hope": "1977-05-25",
}
print(group_movies_by_month_year(movies))

#c
def group_movies_by_month_year(diccionario):
    diccionario_final = {}
    for pelicula, fecha in diccionario.items():
        fecha = fecha.split("-")
        if fecha[0] not in diccionario_final:
            diccionario_final[fecha[0]] = {}
        if fecha[1] not in diccionario_final[fecha[0]]:
            diccionario_final[fecha[0]][fecha[1]] = []
        diccionario_final[fecha[0]][fecha[1]].append(pelicula)
    for anio, meses in diccionario_final.items():
        for mes, peliculas in meses.items():
            diccionario_final[anio][mes] = sorted(peliculas)
    return diccionario_final

"""2. Elegir 3 de los siguientes ordenamientos para conseguir los puntos del examen. (3p)
a. Ordenamiento por Inserción (Insertion Sort): (1p)
Implementa una función que ordene una lista de números utilizando el algoritmo de
ordenamiento por inserción.
b. Ordenamiento por Selección (Selection Sort): (1p)
Implementa una función que ordene una lista de números utilizando el algoritmo de
ordenamiento por selección.
c. Ordenamiento por Fusión (Merge Sort): (1p)
Implementa una función que ordene una lista de números utilizando el algoritmo de
ordenamiento por fusión.
e. Ordenamiento Rápido (Quick Short): (1p)
Implementa una función que ordene una lista de números utilizando el algoritmo de
ordenamiento rápido.
"""
def seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i +1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

lista = [1, 5, 3, 2, 4]
print(seleccion(lista))


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = []
    mayores = []
    for x in lista[1:]:
        if x >= pivote:
            mayores.append(x)
        else:
            menores.append(x)

    menores_ordenandos = quick_sort(menores)
    mayores_ordenandos = quick_sort(mayores)
    return menores_ordenandos + [pivote] + mayores_ordenandos


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) //2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):e
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

"""Implementar un método de la clase
listaEnlazada que elimine sobre la misma lista los
elementos consecutivos repetidos. La clase
listaEnlazada está implementada con una
única referencia al primer nodo."""
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

    def esta_vacia(self):
        return self.prim is None

    def eliminar_repetidos(self):
        if self.prim is None:
            raise ValueError("Lista Vacia")
        actual = self.prim
        while actual is not None and actual.prox is not None:
            if actual.dato == actual.prox.dato:
                actual = actual.prox.prox
            else:
                actual = actual.prox
        return self

"""Crea una clase llamada
persona que tenga dos atributos,
nombre y
edad, y un método
llamado
saludar que imprima un mensaje de saludo con el nombre de la persona."""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola,putito traga mi pito,  mi nombre es", self.nombre)