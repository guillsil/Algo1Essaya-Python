"""a. Escribir una función que dada una lista de tuplas, con el el año en el que se disputó un mundial de
fútbol y el equipo campeón de ese año, devuelva un diccionario con la cantidad de mundiales ganados por
cada equipo. Un ejemplo de la lista de tuplas: [(1930, 'Uruguay'), (1934, 'Italia'), (1938, 'Italia'), ...]
b. Escribir otra función que reciba el diccionario generado en el punto anterior y devuelva una lista con el/los
paises que ganaron más mundiales."""
def mundiales_ganados(lista):
    diccionario = {}
    for tupla in lista:
        if tupla[1] not in diccionario:
            diccionario[tupla[1]] = 1
        else:
            diccionario[tupla[1]] += 1
    return diccionario
print(mundiales_ganados([(1930, 'Uruguay'), (1934, 'Italia'), (1938, 'Italia'), (1950, 'Uruguay'), (1954, 'Alemania'), (1958, 'Brasil'), (1962, 'Brasil'), (1966, 'Inglaterra'), (1970, 'Brasil'), (1974, 'Alemania'), (1978, 'Argentina'), (1982, 'Italia'), (1986, 'Argentina'), (1990, 'Alemania'), (1994, 'Brasil'), (1998, 'Francia'), (2002, 'Brasil'), (2006, 'Italia'), (2010, 'España'), (2014, 'Alemania')]))

def paises_con_mas_mundiales(dic):
    lista = []
    max_mundiales = 0
    for pais in dic:
        if dic[pais] > max_mundiales:
            max_mundiales = dic[pais]
            lista = [pais]
        elif dic[pais] == max_mundiales:
            lista.append(pais)
    return lista
print(paises_con_mas_mundiales(mundiales_ganados([(1930, 'Uruguay'), (1934, 'Italia'), (1938, 'Italia'), (1950, 'Uruguay'), (1954, 'Alemania'), (1958, 'Brasil'), (1962, 'Brasil'), (1966, 'Inglaterra'), (1970, 'Brasil'), (1974, 'Alemania'), (1978, 'Argentina'), (1982, 'Italia'), (1986, 'Argentina'), (1990, 'Alemania'), (1994, 'Brasil'), (1998, 'Francia'), (2002, 'Brasil'), (2006, 'Italia'), (2010, 'España'), (2014, 'Alemania')])))
