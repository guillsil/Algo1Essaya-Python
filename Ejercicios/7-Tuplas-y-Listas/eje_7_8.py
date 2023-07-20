""" Inversión de listas
a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].
b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modi-
fique la lista dada para invertirla, sin usar listas auxiliares."""
LISTA = ['Di', 'buen', 'día', 'a', 'papa']
# a)
def invertir_lista(lista):
    return lista[::-1] # [start:stop:step]
assert invertir_lista(LISTA) == ['papa', 'a', 'día', 'buen', 'Di']
# b)
def invertir_lista2(lista):
    lista.reverse() # reverse() es un método de las listas
    return lista
assert invertir_lista2(LISTA) == ['papa', 'a', 'día', 'buen', 'Di']