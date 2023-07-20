"""Escribir un programa que le pida al usuario que ingrese letras pidiendolas de a una, hasta que ingrese
una cadena vacía. Si ingresa algo que no es una letra, o ingresa más de una, debe ignorarse esta entrada.
Luego debe imprimir todas las letras ingresadas en orden alfabético.
Ejemplo: Se ingresa "g", "n", "a", "v", "1", "n", "p", "aa", "n"; se debe imprimir agnnnpv."""

def pedir_letras():
    """Pide letras al usuario hasta que ingrese una cadena vacía"""
    lista = []
    letra = input("Ingrese una letra: ")
    while letra != "":
        if len(letra) == 1 and letra.isalpha():
            lista.append(letra)
        letra = input("Ingrese una letra: ")
    return lista

def ordenar_letras(lista):
    """Ordena las letras de la lista alfabéticamente"""
    lista.sort()
    return lista

def main():
    """Función principal"""
    print(ordenar_letras(pedir_letras()))
main()
