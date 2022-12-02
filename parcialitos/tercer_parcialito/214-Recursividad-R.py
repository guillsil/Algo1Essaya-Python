"""Escribir una función recursiva que dado un número N genere una lista de enteros, con la
forma [-N, -N+1, ..., -1, 0, 1, ..., N-1, N]. Por ejemplo para N = 2 debe devolver [-2, -1, 0, 1, 2].
Asumir que N >= 0"""
def generar_lista(n):
    """Escribir una funcion recursiva que dado un numero N genere una lista de enteros, con la forma
    [-N, -N+1, ..., -1, 0, 1, ..., N-1, N]."""
    lista = []
    for i in range(-n, n+1):
        lista.append(i)
    return lista

def generar_recursivo(n):
    if n == 0:
        return [0]
    else:
        lista = generar_recursivo(n-1)
        lista.append(n)
        lista.insert(0, -n)
        return lista
print(generar_recursivo(2))