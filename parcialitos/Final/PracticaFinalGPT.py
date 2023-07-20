"""Ejercicio 1: Recursividad y listas

Implementar una función recursiva llamada suma_lista que reciba una lista de números enteros y devuelva la suma de todos los elementos de la lista.

Ejemplo:
lista = [1, 2, 3, 4, 5]
print(suma_lista(lista))  # Salida: 15
"""
#iterativa
def suma_lista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
lista = [1, 2, 3, 4, 5]
#print(suma_lista(lista))  # Salida: 15

#recursiva
def suma_lista2(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista2(lista[1:])
lista = [1, 2, 3, 4, 5]
#print(suma_lista2(lista))  # Salida: 15
#print("hola")
    

"""En un país hipotético, el gobierno está desarrollando un sistema de recomendación de películas basado en la
inteligencia artificial. Implementar la función recomendar_peliculas(peliculas, genero, duracion_maxima) que 
reciba una lista de diccionarios de películas, donde cada diccionario contiene información como el título, el 
género y la duración de la película. La función debe devolver una lista con los títulos de las películas que 
pertenecen al género especificado y tienen una duración menor o igual a la duración máxima.
"""

def recomendar_peliculas(peliculas, genero, duracion_max):
    lista_peliculas = []
    for peli in peliculas:
        if peli["genero"] == genero and peli["duracion"] <= duracion_max:
            lista_peliculas.append(peli["titulo"])
    return lista_peliculas


peliculas = [
    {"titulo": "La La Land", "genero": "Romance", "duracion": 126},
    {"titulo": "Inception", "genero": "Ciencia ficción", "duracion": 148},
    {"titulo": "The Dark Knight", "genero": "Acción", "duracion": 150},
    {"titulo": "The Shawshank Redemption", "genero": "Drama", "duracion": 142}
]
genero = "Acción"
duracion_maxima = 150

#print(recomendar_peliculas(peliculas, genero, duracion_maxima))  # Salida: ["The Dark Knight"]

"""La tecnología de reconocimiento de voz se ha vuelto cada vez más popular en los asistentes virtuales. 
Implementar la función contar_vocales_frase(frase) que reciba una frase y utilice inteligencia artificial para
contar el número de vocales presentes en la misma. La función debe devolver un diccionario donde las claves
son las vocales (a, e, i, o, u) y los valores son la cantidad de veces que cada vocal aparece en la frase
"""

def contar_vocales_frase(frase):
    diccionario = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for caracter in frase:
        if caracter == "a":
            diccionario["a"] += 1
        elif caracter == "e":
            diccionario["e"] += 1
        elif caracter == "i":
            diccionario["i"] += 1
        elif caracter == "o":
            diccionario["o"] += 1
        elif caracter == "u":
            diccionario["u"] += 1
    return diccionario

frase = "Hola, cómo estás?"
conteo_vocales = contar_vocales_frase(frase)
#print(conteo_vocales)  # Salida: {'a': 1, 'e': 1, 'i': 0, 'o': 2, 'u': 0}



"""La ciberseguridad es un tema de suma importancia en la actualidad. Implementar la función validar_contrasena
(contrasena) que reciba una contraseña y utilice técnicas de inteligencia artificial para verificar su 
fortaleza. La función debe evaluar la contraseña en función de su longitud, uso de caracteres especiales, 
combinación de letras mayúsculas y minúsculas, y otros criterios. Devolver un valor de verdad que indique si 
la contraseña es considerada segura o no."""


