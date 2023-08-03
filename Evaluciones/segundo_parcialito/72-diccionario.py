"""a.Escribir una función que dado un texto, devuelva un diccionario con la frecuencia de cada palabra del texto.
b. Escribir una función que reciba un diccionario como el generado por la función del ítem a y devuelva una
lista con la/s palabras que tienen la máxima frecuencia.
"""
def frecuencia_palabras(texto):
    diccionario = {}
    for palabra in texto.split():
        if palabra not in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1
    return diccionario

def maxima_frecuencia(dic):
    lista = []
    max_frecuencia = 0
    for palabra in dic:
        if dic[palabra] > max_frecuencia:
            max_frecuencia = dic[palabra]
            lista = [palabra]
        elif dic[palabra] == max_frecuencia:
            lista.append(palabra)
    return lista
print(maxima_frecuencia(frecuencia_palabras("Aquí podés obtener un ejercicio aleatorio de cualquier tema de la materia, para practicar para los Evaluciones. Los ejercicios presentados aquí son reales y fueron tomados en alguna fecha pasada. Los ejercicios son aleatorios, por lo que cada vez que recargás la página te aparecerá uno distinto. Si querés practicar con un ejercicio en particular, podés buscarlo en la lista de ejercicios. Si querés practicar con un tema en particular, podés buscarlo en la lista de temas. Si querés practicar con un parcialito en particular, podés buscarlo en la lista de Evaluciones. Si querés practicar con un ejercicio en particular, podés buscarlo en la lista de ejercicios. Si querés practicar con un tema en particular, podés buscarlo en la lista de temas. Si querés practicar con un parcialito en particular, podés buscarlo en la lista de Evaluciones. Si querés practicar con un ejercicio en particular, podés buscarlo en la lista de ejercicios. Si querés practicar con un tema en particular, podés buscarlo en la lista de temas. Si querés practicar con un parcialito en particular, podés buscarlo en la lista de Evaluciones. Si querés practicar con un ejercicio en particular, podés buscarlo en la lista de ejercicios. Si querés practicar con un tema en particular, podés buscarlo en la lista de temas. Si querés practicar con un parcialito en particular, podés buscarlo en la lista de Evaluciones. Si querés practicar con un ejercicio en particular, podés buscarlo en la lista de ejercicios. Si querés practicar con un tema en particular, podés buscarlo en la lista de temas. Si querés practicar con un parcialito en particular, podés buscarlo en la lista de Evaluciones. Si querés practicar con un ejercicio en particular, podés buscarlo en la lista de ejercicios. Si querés practicar con un tema en particular, podés buscarlo en la lista de temas. Si querés practicar con un parcialito en particular, podés buscarlo en la lista de Evaluciones. Si querés practicar con un ejercicio en particular, podés buscarlo en la lista de ejercicios. Si querés practicar con un tema en particular, podés buscar")))