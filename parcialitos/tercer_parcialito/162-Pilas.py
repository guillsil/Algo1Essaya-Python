from pila import Pila
"""EScribir una función intercalar(pilas) que reciba una secuencia de pilas y devuelva una pila con los elementos de todas 
las pilas intercalados, manteniendo el orden relativo. Las pilas originales deben quedar vacías. Ejemplo:
intercalar([Pila(1, 2), Pila(3, 4, 5, 6), Pila(7)])
   → Pila(1, 3, 7, 2, 4, 5, 6)"""
def intercalar(pilas):
    """Devuelve una pila con los elementos de todas las pilas intercalados, manteniendo el orden relativo.
    Las pilas originales deben quedar vacías."""
    pila = Pila()


pila1 = Pila()
pila1.apilar(1)
pila1.apilar(2)

pila2 = Pila()
pila2.apilar(3)
pila2.apilar(4)
pila2.apilar(5)
pila2.apilar(6)

pila3 = Pila()
pila3.apilar(7)

print(intercalar([pila1, pila2, pila3]))