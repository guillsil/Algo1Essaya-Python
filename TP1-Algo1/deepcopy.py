
def copia_profunda(lista):
    """Realiza una copia profunda de una lista con sus sublistas y develve la misma sin modificar la original"""
    copia = []
    for i in lista:
        copia.append(i[:])
    return copia
def main():
    lista = [[1,2,3],[4,5,6],[7,8,9]]
    copia = copia_profunda(lista)
    print(copia)
    lista[0][0] = 0
    print(lista)
    print(copia)
main()