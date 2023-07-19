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


"""3. Implementar la función pascal (n: int) -> list[list[int]] que devuelve una lista con las 
primeras n filas del triángulo de Pascal. Ejemplo:
pascal (4) -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
Nota: en el triángulo de Pascal, cada elemento es la suma de los dos elementos que están en
la fila superior:
    1
   1 1
  1 2 1
 1 3 3 1
"""
#iterativo
def pascal(n):
    lista = []
    for i in range(n):
        lista.append([1])
        for j in range(1, i):
            lista[i].append(lista[i-1][j-1] + lista[i-1][j])
        if i != 0:
            lista[i].append(1)
    return lista
print(pascal(4))




