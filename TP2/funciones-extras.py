def grilla_a_diccionario(grilla):
    """"devuelve un diccionario donde la clave es la posicion de cada elemento y el valor es el simbolo que representa"""
    diccionario = {}
    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            diccionario[grilla[i][j]] = LISTA_DE_SIMBOLOS[i]
    return diccionario


def imprimir_grilla(grilla):
    """Imprime la grilla"""
    diccionario = grilla_a_diccionario(grilla)
    for i in range(grilla[4][1]):
        for j in range(grilla[4][0]):
            if (j,i) in diccionario:
                print(diccionario[(j,i)], end="")
            else:
                print(" ", end="")
        print()