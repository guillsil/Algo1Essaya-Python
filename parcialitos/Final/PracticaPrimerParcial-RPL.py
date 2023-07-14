"""
Escribir un programa que imprima los números de 1 a 100; pero para los múltiplos de 3 imprima "Miki"
 en lugar del número; y para los múltiplos de 5 imprima "Moko". Para los múltiplos de 3 y 5 debe
  imprimir "MikiMoko".
"""
def mikimoko():
    for i in range(1,100):
        if i % 3 == 0 and i % 5 == 0:
            print("MikiMoko")
        elif i % 3 == 0:
            print("Miki")
        elif i % 5 == 0:
            print("Moko")
        else:
            print(i)

#mikimoko()

"""
Un bigrama es una secuencia de dos palabras contiguas dentro de un texto. Escribir una función que reciba un 
texto y devuelva una lista con todos sus bigramas. Los mismos deberán estar representados con una tupla (, ). 
Ejemplo:

>>> obtener_bigramas("Uno se alegra de resultar útil")
[('Uno', 'se'), ('se', 'alegra'), ('alegra', 'de'), ('de', 'resultar'), ('resultar', 'útil')]
"""
def obtener_bigramas(texto):
    lista = []
    palabras = texto.split()
    for i in range(len(palabras)-1):
        lista.append((palabras[i], palabras[i+1]))
    return lista
#print(obtener_bigramas("Uno se alegra de resultar útil"))

"""
Escribir una función que reciba una lista de tuplas de la forma (n, m) y devuelva dos listas.

    La primera tendrá los elementos de la primer posicion de las tuplas
    La segunda, los que estén en la segunda posición.

Ejemplo:

>>> partir_tuplas([(1,2),(1,2),(1,2),(8,9)]
([1,1,1,8],[2,2,2,9])
"""
def separarar_tupla(lista):
    izq = []
    der = []
    for tupla in lista:
        izq.append(tupla[0])
        der.append((tupla[1]))
    return (izq, der)

#print(separarar_tupla([(1,2), (1,2), (1, 2), (8, 9)]))

"""
Escribir un programa que le pida al usuario que ingrese un número entero positivo n y una cadena, e 
imprima la misma cadena pero con un guión (-) cada n lugares.

Ejemplo: n = 2, cadena = Esto es un ejemplo.; debe imprimir Es-to- e-s -un- e-je-mp-lo-.

Ingrese una frecuencia: 2
Ingrese una frase: Esto es un ejemplo.
Es-to- e-s -un- e-je-mp-lo-.

Otro ejemplo: n = 1, cadena = Otra frase devuelta; debe imprimir O-t-r-a- -f-r-a-s-e- -d-e-v-u-e-l-t-a

Ingrese una frecuencia: 1
Ingrese una frase: Otra frase devuelta
O-t-r-a- -f-r-a-s-e- -d-e-v-u-e-l-t-a
"""


