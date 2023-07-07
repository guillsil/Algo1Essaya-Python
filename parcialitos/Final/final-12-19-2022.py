"""En un país hipotético el gobierno se dio cuenta de que puede redefinir de forma automática
sus políticas de subsidios a los servicios cruzando listados de diferentes organismos.
Implementar la funcion mantienen_subsidio(titulares, salarios_altos) donde ambos pará-
metros son listas ordenadas de números de DNI, siendo titulares el listado de los titulares
de servicios, y salarios_altos el listado de las personas que cobran más de $350.000 al mes.
La función debe devolver en tiempo lineal una lista con los números de DNI de las personas
que mantienen su subsidio, es decir las que no tienen salario alto"""
def mantinen_subsidio(titulares, salarios_altos):
    lista_beneficiarios = []
    diccionario = {}
    for dni in titulares:
        if dni not in diccionario:
            diccionario[dni] = True
    for previlegiados in salarios_altos:
        if previlegiados in diccionario:
            diccionario.pop(previlegiados)
    
    lista_beneficiarios = list(diccionario.keys())
    return lista_beneficiarios

titulares = [1,2,3,4,5,6,7,8,9,10]
salarios_altos = [1,4,5,6,7,8]
#debe devovler [2,3,9,10]
#print(mantinen_subsidio(titulares, salarios_altos))
"""Implementar la función splitlines(s) que recibe una lista de cadenas y se comporta igual que
s.split('\n'). No se permite usar ningún método de str. Ejemplo:
>>> splitlines("hola\nque\ntal")
['hola', 'que', 'tal']"""

SEPARADOR = "\n"

def splitlnes(string):
    resultado = []
    subcadena = "" 
    for caracter in string:
        if caracter != SEPARADOR:
            subcadena += caracter
        else:
            resultado.append(subcadena)
            subcadena = ""
    resultado.append(subcadena)
    return resultado

#print(splitlnes("hola\nque\ntal"))

"""Un árbol binario es una estructura enlazada en la que cada nodo contiene referencias a otros
dos nodos, llamados hijo izquierdo y derecho (pudiendo cualquiera de ellos ser una referencia
nula). Se denomina raíz al primer nodo del árbol, y hojas a aquellos nodos del árbol que no
tienen hijo izquierdo ni derecho.
a. Implementar la clase Nodo que representa un nodo del árbol binario.
b. Implementar la función invertir(raiz) que recibe el nodo raíz y devuelve una copia del
árbol en el que todos los hijos están invertidos.
Sugerencia: pensar la función en forma recursiva."""
class Nodo():
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der
    def invertir(self):
        if self.izq is None and self.der is None:
            raise ValueError("El nodo no tiene hijos")
        
        if self.izq is not None:
            self.izq = self.izq.invertir()
        if self.der is not None:
            self.der = self.der.invertir()
        self.izq, self.der = self.der, self.izq
        return self
    
"""Se tiene un archivo CSV con formato barrio;calle;longitud (por ejemplo: San Telmo,Av.
Paseo Colón,1500).
Implementar la función calles_mas_largas que recibe el nombre del archivo CSV y devuelve
un diccionario cuyas claves son los barrios y el valor es una tupla (calle, hlongitud) corres-
pondiente a la calle más larga del barrio."""

import csv
def calles_mas_largas(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        diccionario = {}
        archivo_reader = csv.reader(archivo)
        for barrio, calle, longitud in archivo_reader:
            if barrio not in diccionario:
                diccionario[barrio] = (calle, longitud)
            else:
                if diccionario[barrio][1] < longitud:
                    diccionario[barrio] = (calle, longitud)
                else:
                    diccionario[barrio] = (diccionario[barrio][0], diccionario[barrio][1])

    return diccionario

"""Dada la clase Cola con los métodos __init__, esta_vacia, encolar y desencolar, implementar
la clase ColaConCapacidadMaxima, que tenga los mismos métodos de Cola, y además:
• En el constructor debe recibir la capacidad máxima.
• Al encolar debe lanzar una excepción si no hay capacidad disponible.
• Debe tener un método esta_llena() que indica si la cola está llena o no, en tiempo constante."""
from cola import Cola

class ColaConCapacidadMaxima(Cola):
    def __init__(self, capacidad_maxima):
        super().__init__()
        self.capacidad_maxima = capacidad_maxima
        self.cantidad_elementos = 0

    def encolar(self, dato):
        if self.cantidad_elementos == self.capacidad_maxima:
            raise ValueError("La cola esta llena")
        else:
            self.cantidad_elementos += 1
            return super().encolar(dato)
        

                    




    
    
        

            

        
                
