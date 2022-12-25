"""1. Representamos un intervalo de tiempo de la forma (a, b), siendo a el instante en el que
comienza el intervalo y b el instante en el que finaliza (a < b).
Escribir una función que reciba una lista de intervalos ordenados por el valor de a y devuelva
una lista en la que los intervalos superpuestos hayan sido combinados. Por ejemplo, los inter-
valos (1, 4) y (3, 5) se combinan obteniendo (1, 5). Si el fin y el inicio de dos intervalos son
exactamente iguales, se considera que son superpuestos.
Ejemplo: combinar_intervalos([(1,5), (2,3), (4,6), (7h,8), (8,10), (12,15)]) ➡ [(1,6),
(7,10), (12,15)]"""
def combinar_intervalos(lista):
    """Recibe una lista de intervalos ordenados por el valor de a y devuelve una lista en la que los intervalos superpuestos hayan sido combinados."""
    i = 0
    while i < len(lista) - 1:
        if lista[i][1] >= lista[i + 1][0]:
            lista[i] = (lista[i][0], max(lista[i][1], lista[i + 1][1]))
            lista.pop(i + 1)
        else:
            i += 1
    return lista
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
def es_palabras(contrasenia, palabras):
    """Determina si una contraseña que contiene únicamente letras minúsculas está formada por una secuencia de palabras."""
    if contrasenia == '':
        return True
    for palabra in palabras:
        if contrasenia.startswith(palabra): #startswith() devuelve True si la cadena comienza con la subcadena especificada.
            return es_palabras(contrasenia[len(palabra):], palabras)
    return False
print(es_palabras('agua', palabras))
print(es_palabras('auga', palabras))
print(es_palabras('aguaaire', palabras))
print(es_palabras('aguaire', palabras))
print(es_palabras('auga', palabras))
print(es_palabras('aguaagua', palabras))
