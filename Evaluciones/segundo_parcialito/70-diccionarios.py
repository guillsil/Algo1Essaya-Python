"""Se cuenta con un diccionario cuyas claves son títulos de películas, y su valor asociado su fecha de
estreno, una cadena en formato DD/MM/AAAA. Escribir una función que dado un diccionario de estas características,
devuelva otro diccionario cuyas claves sean el mes y el año en formato MM/AAAA, y su valor una lista con todas las
películas que se estrenaron en dicho mes y año."""
def peliculas_por_mes_y_año(dic):
    diccionario = {}
    for pelicula in dic:
        fecha = dic[pelicula].split('/')
        mes_año = fecha[1] + '/' + fecha[2]
        if mes_año not in diccionario:
            diccionario[mes_año] = [pelicula]
        else:
            diccionario[mes_año].append(pelicula)
    return diccionario
print(peliculas_por_mes_y_año({"El padrino": "24/03/1972", "El padrino 2": "20/12/1974", "El padrino 3": "12/12/1990", "El padrino 4": "12/12/1990", "El padrino 5": "12/12/1990"}))