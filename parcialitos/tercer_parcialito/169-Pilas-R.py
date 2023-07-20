"""Se quiere escribir una función que sea capaz de sumar dos números que se encuentran representados como pilas
de sus dígitos. Los números a sumar pueden tener cualquier cantidad de dígitos, y a su vez, no tener la misma
cantidad de dígitos uno que el otro. La función debe devolver una pila con los dígitos del resultado. Por ejemplo,
para realizar la suma 641 + 789 se tendrían las siguientes pilas:
p1 = | 6 | (tope)
     | 4 |
     | 1 |
     |---|
y
p2 = | 7 | (tope)
     | 8 |
     | 9 |
     |---|

La función debería devolver la siguiente pila

| 1 | (tope), que representa al número 1430.
| 4 |
| 3 |
| 0 |
|---|

Hint: para sumar los números conviene empezar sumando desde los dígitos menos significativos (los que se encuentran al
fondo de la pila).
"""
from pila import Pila
def sumar_pilas(p1, p2):
    pila_resultado = Pila()
    acarreo = 0
    while not p1.esta_vacia() or not p2.esta_vacia():
        if not p1.esta_vacia():
            digito1 = p1.desapilar()
        else:
            digito1 = 0
        if not p2.esta_vacia():
            digito2 = p2.desapilar()
        else:
            digito2 = 0
        suma = digito1 + digito2 + acarreo
        acarreo = suma // 10
        digito_resultado = suma % 10
        pila_resultado.apilar(digito_resultado)
    if acarreo > 0:
        pila_resultado.apilar(acarreo)
    return pila_resultado
p1 = Pila()
p1.apilar(6)
p1.apilar(4)
p1.apilar(1)

p2 = Pila()
p2.apilar(7)
p2.apilar(8)
p2.apilar(9)

resultado = sumar_pilas(p1, p2)
print(resultado)
