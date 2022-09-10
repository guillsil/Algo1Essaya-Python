"""Escribir una función que reciba dos números como parámetros, y devuelva cuán-
tos múltiplos del primero hay, que sean menores que el segundo.
a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que
sea mayor que el segundo.
c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operacio-
nes?"""
# a)
def multiplos(n1, n2):
    contador = 0
    for i in range(n1, n2):
        if i % n1 == 0:
            contador += 1
    return contador
print(multiplos(2, 100))
# b)
def multiplosb(n1, n2):
    contador = 0
    i = n1
    while i < n2:
        if i % n1 == 0:
            contador += 1
        i += n1
    return contador
print(multiplosb(2, 100))
# c) Para mi la manera mas clara es la b, ya que es mas facil de entender, y realiza menos operaciones que la a, ya que no hace un ciclo innecesario.
