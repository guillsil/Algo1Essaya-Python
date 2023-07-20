"""Se tiene un diccionario de la forma {nombre_vendedor : total_vendido}, con la suma total de lo vendido por
distintos vendedores, y otro con forma {local : [nombre_vendedor_1, nombre_vendedor_2, …]}, con los vendedores
que trabajan en cada local. Escribir una función que reciba diccionarios como los mencionados, y devuelva un
nuevo diccionario cuyas claves sean los nombres de los locales y sus valores el total vendido por los vendedores
de ese local."""
def total_por_local(dic_vendedores, dic_locales):
    diccionario = {}
    for local in dic_locales:
        total = 0
        for vendedor in dic_locales[local]:
            total += dic_vendedores[vendedor]
        diccionario[local] = total
    return diccionario