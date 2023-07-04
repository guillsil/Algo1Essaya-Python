"""Implementar una función recursiva que dada una cadena, devuelva la cantidad de veces que aparece el primer caracter (sin contar la primera aparición), en las posiciones pares de la cadena. Ej:

    Para "No es tan fácil, que todo te salga bien" debe devolver 2
    Para "No es tan fácil que todo te salga bien" debe devolver 1

"""
def cantidad_de_apariciones(cadena):
    # Caso base
    if len(cadena) < 3:
        return 0

    # Caso recursivo
    primer_caracter = cadena[0]
    subcadena = cadena[2:]

    if primer_caracter == subcadena[0]:
        return 1 + cantidad_de_apariciones(subcadena)
    else:
        return cantidad_de_apariciones(subcadena)





  
cadena = "No es tan fácil, que todo te salga bien"

print(cantidad_de_apariciones(cadena))
cadena = "No es tan fácil que todo te salga bien"
print(cantidad_de_apariciones(cadena))