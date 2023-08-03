"""1. Se tiene una lista de números positivos y se quiere saber si es posible sumar un subconjunto de
los números de esa lista para obtener un resultado particular. Por ejemplo, con la lista [ 1, 5,
7, 2) se puede obtener el valor 7 de dos maneras posibles (7, 5+2) pero no puede obtenerse el
valor 4 0 el 11. Implementar la función puede _ sumar (numeros:      list(intl, objetivo: int)
->> bool que indique si esa lista de números puede sumar el objetivo o no. Por ejemplo:
puede_sumar((l, 5, 7, 21, 7) True
puede_sumar((l, 5, 7, 2), 11) False
Ayuda: pensar la función en forma recursiva."""

#iterativo
def puede_sumar(numeros, objetivo):
    for i in range(len(numeros)):
        for j in range(len(numeros)):
            if numeros[i] + numeros[j] == objetivo:
                return True
    return False
print(puede_sumar([1, 5, 7, 2], 7))
print(puede_sumar([1, 5, 7, 2], 11))

#recursivo
def puede_sumar(numeros, objetivo):
    if len(numeros) == 0:
        return False
    if numeros[0] == objetivo:
        return True
    return puede_sumar(numeros[1:], objetivo) or puede_sumar(numeros[1:], objetivo - numeros[0])
print(puede_sumar([1, 5, 7, 2], 7))
print(puede_sumar([1, 5, 7, 2], 11))

"""Escribir la clase NumeroRacional con los siguientes metodos:
init que recibe el numerador y denominador. Debe lanzar una excepción si el denomi-
nador es O.
f loat que devuelve el racional convertido a punto flotante.
add que suma dos racionales.
• mul que multiplica dos racionales.
• simplificar que devuelve un nuevo racional simplificando el numerador y denominador.
Nota: Se permite usar la función gcd del módulo math que devuelve eI máximo común divisor
entre dos números."""
import math
class Numerocional():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0")

    def __float__(self):
        return float(self.numerador / self.denominador)

    def __add__(self,numerador_otro, denominador_otro):
        return Numerocional(self.numerador * denominador_otro + self.denominador * numerador_otro, self.denominador * denominador_otro)

    def __mul__(self, numerador_otro, denominador_otro):
        return Numerocional(self.numerador * numerador_otro, self.denominador * denominador_otro)

    def simplificar(self):
        mcd = math.gcd(self.numerador, self.denominador)
        return Numerocional(self.numerador // mcd, self.denominador // mcd)



#iterativo
def pascal(n):
    lista = []
    for i in range(n):
        lista.append([])
        lista[i].append(1)
        for j in range(1, i):
            lista[i].append(lista[i-1][j-1] + lista[i-1][j])
        if(n != 0):
            lista[i].append(1)
    return lista
print(pascal(4))

"""4. Sea un archivo CSV que contiene el historial de tráfico de un sitio web, medido en cantidad de
usuarios conectados, con el formato año, mes , día, cant_min, cant_media,cant_max (por ejemplo
2626,61, 10,2214 ,5389, 11876).
Escribir una función que recibe la ruta del archivo y devuelve un diccionario con la cantidad
máxima de usuarios conectados de cada año,
Cada fecha aparece a l0 sumo una vez. No se puede asumir que todas las fechas están en el
archivo, o que están ordenadas. En caso de error al procesar una línea, ignorarla y pasar a la
siguiente."""
import csv
def cant_max_reproducciones(ruta_archivo):
    diccionario = {}
    try:
        with open(ruta_archivo, "r") as archivo:
            archivo_reader = csv.reader(archivo)
            for linea in archivo_reader:
                if len(linea) != 6:
                    raise ValueError("El archivo no tiene el formato correcto (1)")

                if linea[0] not in diccionario:
                    diccionario[linea[0]] = linea[5]
                else:
                    """si el año ya esta debo sumar la cantidad de reproducciones"""
                    diccionario[linea[0]] = int(diccionario[linea[0]]) + int(linea[5])
    except FileNotFoundError:
        print("El archivo no existe")
    return diccionario
print(cant_max_reproducciones("archivo.csv"))


"""Implementar el metodo intercambiar_pares de la clase ListaEnlazada que intercambia cada par de elementos.
Por ejemplo:
lista = ListaEnlazada([1, 2, 3, 4, 5, 6, 7, 8, 9])
lista.intercambiar_pares()
lista.imprimir() # imprime 2 1 4 3 6 5 8 7 9
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

    def intercambiar_pares(self):
        nueva = ListaEnlazada()
        if self.prim is None:
            raise ValueError("La lista esta vacia")

        actual = self.prim
        while actual is not None and actual.prox is not None:
            nueva.agregar(actual.prox.dato)
            nueva.agregar(actual.dato)
            actual = actual.prox.prox
        if actual is not None:
             nueva.agregar(actual.dato)
        return nueva

    def intercambiar2(self):
        if self.prim is None:
            raise ValueError("La lista esta vacia")

        actual = self.prim
        while actual is not None and actual.prox is not None:
            actual.dato, actual.prox.dato = actual.prox.dato, actual.dato
            actual = actual.prox.prox
        return self



lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
lista.agregar(7)
print(lista)
print(lista.intercambiar_pares())
print(lista.intercambiar2())
