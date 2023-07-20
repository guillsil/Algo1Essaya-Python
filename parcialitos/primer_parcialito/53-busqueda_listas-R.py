"""a) Hacer el seguimiento paso por paso de la búsqueda del número 5 en la lista [1,2,4,5,6,8,9,11,14], utilizando
el algoritmo de búsqueda binaria.
b) ¿Qué condiciones debe cumplir sí o sí una lista para que se pueda realizar una búsqueda binaria sobre ella?
c) Si una lista cumple las condiciones del punto (b) y tiene elementos repetidos, ¿puede aplicarse igual una búsqueda
binaria sobre ella?
"""
# a) [1,2,4,5,6,8,9,11,14]
#    izquierda = 0
#    derecha = 8
#    medio = (0 + 8) // 2 = 4
#    lista[medio] = 6
#    5 < 6
#    izquierda = medio + 1 = 5
#    derecha = 8
#    medio = (5 + 8) // 2 = 6
#    lista[medio] = 9
#    5 < 9
#    izquierda = medio + 1 = 7
#    derecha = 8
#    medio = (7 + 8) // 2 = 7
#    lista[medio] = 11
#    5 < 11
#    izquierda = medio + 1 = 8
#    derecha = 8
#    medio = (8 + 8) // 2 = 8
#    izquierda > derecha
#    return -1
# b) La lista debe estar ordenada de forma creciente o decreciente.
# c) Si la lista tiene elementos repetidos, la búsqueda binaria no puede aplicarse igual, ya que no se puede