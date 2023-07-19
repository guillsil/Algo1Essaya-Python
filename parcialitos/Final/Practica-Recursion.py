"""Calcular el factorial de un número:
Implementa una función recursiva que calcule el factorial de un número entero dado. El factorial de un
número n se calcula multiplicando todos los números desde 1 hasta n."""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)
#print(factorial(4))

"""Calcular la suma de los elementos de una lista:
Implementa una función recursiva que calcule la suma de todos los elementos de una lista de números enteros.

Ejemplo:"""

def suma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma(lista[1:])

lista = [1, 2, 3, 4, 5]
#print(suma(lista))

"""Calcular el número de elementos de una lista:
Implementa una función recursiva que calcule el número de elementos de una lista.

Ejemplo:"""

def tamanio(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + tamanio(lista[1:])

#print(tamanio(lista))

"""Verificar si una cadena es un palíndromo:
Implementa una función recursiva que verifique si una cadena es un palíndromo, es decir, si se lee
igual de izquierda a derecha que de derecha a izquierda.

Ejemplo:"""

def palindromo(cadena):
    if len(cadena) <=1:
        return True
    elif cadena[0] != cadena[-1]:
        return False
    else:
        return palindromo(cadena[1:-1])

#print(palindromo("reconocer"))
#print(palindromo("hola"))

"""Calcular la potencia de un número:
Implementa una función recursiva que calcule la potencia de un número entero dado. 
La potencia de un número base elevado a un exponente se calcula multiplicando la base 
por sí misma el número de veces igual al exponente.
"""
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base*potencia(base, exponente-1)

#print(potencia(2,4))
#print(potencia(2, 3))

"""Generar la secuencia de Fibonacci:
Implementa una función recursiva que genere los primeros n términos de la secuencia de Fibonacci. 
La secuencia de Fibonacci comienza con 0 y 1, y cada término posterior es la suma de los dos
términos anteriores."""
def finonacci(n):
    if n <= 1:
        return n
    else:
        return finonacci(n-1) + finonacci(n-2)

#for i in range(3):
#    print(finonacci(i))

"""Calcular el máximo común divisor (MCD) de dos números:
Implementa una función recursiva que calcule el máximo común divisor (MCD) de dos números enteros.
El MCD de dos números es el número más grande que los divide sin dejar residuo."""

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)

#print(mcd(48,36))

"""Imprimir los elementos de una lista en orden inverso:
Implementa una función recursiva que imprima los elementos de una lista en orden inverso."""
def imprimir_reverso(lista):
    if len(lista) == 0:
        return
    else:
        print(lista[-1])
        imprimir_reverso(lista[:-1])

imprimir_reverso(lista)

"""Encontrar el número de combinaciones:
Implementa una función recursiva que calcule el número de combinaciones posibles de tomar k elementos de
un conjunto de n elementos. Utiliza la fórmula matemática de combinaciones: C(n, k) = C(n-1, k-1) + C(n-1, k)."""

def combinaciones(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return combinaciones(n - 1, k - 1) + combinaciones(n - 1, k)

print(combinaciones(5, 3))  # Output: 10
print(combinaciones(10, 5))  # Output: 252

"""Resolver el problema de las Torres de Hanoi:
Implementa una función recursiva que resuelva el problema de las Torres de Hanoi. El objetivo es mover una torre
de discos desde un poste de origen a un poste de destino, utilizando un poste auxiliar. Los discos deben ser
movidos de uno en uno, y en ningún momento puede haber un disco de mayor tamaño encima de uno de menor tamaño"""
def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        hanoi(n - 1, auxiliar, destino, origen)

hanoi(3, 'A', 'C', 'B')

"""Contar la cantidad de números pares en una lista:
Implementa una función recursiva que reciba una lista de números y devuelva la cantidad de números 
pares que contiene."""

def pares(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] % 2 == 0:
            return 1 + pares(lista[1:])
        else:
            return pares(lista[1:])
lista = [1, 2, 3,4,5]
print(pares(lista))

def impares(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] % 2 != 0:
            return 1 + pares(lista[1:])
        else:
            return pares(lista[1:])
print(impares(lista))

"""VSumar los dígitos de un número:
Implementa una función recursiva que sume todos los dígitos de un número entero."""
def sumar_digitos(n):
    if n <= 10:
        return n
    else:
        return n %10 + sumar_digitos(n //10)

print(sumar_digitos(12345))

"""Encontrar el máximo elemento en una lista:
Implementa una función recursiva que encuentre el elemento máximo en una lista de números."""
def elemento_max(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] > elemento_max(lista[1:]):
            return lista[0]
        else:
            return elemento_max(lista[1:])
lista = [1, 2, 3,4,5]
print(elemento_max(lista))

"""Verificar si una lista está ordenada de forma ascendente:
Implementa una función recursiva que verifique si una lista de números está ordenada de forma ascendente."""
def esta_ordenada(lista):
    if len(lista) <= 1:
        return True
    else:
        if lista[0] <= lista[1]:
            return esta_ordenada(lista[1:])
        else:
            return False

print(esta_ordenada([1, 2, 3, 4, 5]))  # Output: True

"""Verificar si un número es primo:
Implementa una función recursiva que verifique si un número dado es primo."""
def es_primo(n, divisor=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor ** 2 > n:
        return True
    return es_primo(n, divisor + 1)

print(es_primo(7))  # Output: True

"""
Generar todos los subconjuntos de una lista:
Implementa una función recursiva que genere todos los subconjuntos de una lista dada.
Ejemplo:
subconjuntos([1, 2, 3]) = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]"""

def generar_subconjuntos(lista):
    if len(lista) == 0:
        return [[]]
    else:
        subconjuntos_anteriores = generar_subconjuntos(lista[:-1])
        nuevos_subconjuntos = [conjunto + [lista[-1]] for conjunto in subconjuntos_anteriores]
        return subconjuntos_anteriores + nuevos_subconjuntos


