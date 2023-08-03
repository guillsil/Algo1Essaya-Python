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



"""a) Implementar la clase Rectangulo, con los siguientes métodos:

    __init__(self, base, altura): Crea un rectángulo a partir de la longitud de su base y altura.
Debe lanzar una excepción si alguno de los valores es negativo.
    perimetro(self): Calcula el perímetro del rectángulo.
    area(self): Calcula el área del rectángulo.

b) Implementar el o los métodos necesarios para que al ordenar una lista de rectángulos, se 
ordene automáticamente por sus respectivas áreas. Es decir, para que el siguiente ejemplo funcione:
rectangulos = [
    Rectangulo(3, 4),
    Rectangulo(1, 2),
    Rectangulo(5, 6),
]
rectangulos.sort()  # Ordena por área
print(rectangulos)  # Muestra el resultado
# Salida: [Rectangulo(1, 2), Rectangulo(3, 4), Rectangulo(5, 6)]
"""
class Rectangulo:
    def __init__(self, base , altura):
        if base < 0 or altura < 0:
            raise ValueError("Valores ingresados son incorrectos")
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2*(self.altura + self.base)

    def area(self):
        return self.base * self.altura

    def __str__(self):
        return f"Rectangulo({self.base}, {self.altura})"
class Rectangulos:
    def __init__(self):
        self.rectangulos = []

    def agregar_rectangulo(self, rectangulo):
        self.rectangulos.append(rectangulo)

    def __str__(self):
        return str(self.rectangulos)

    def sort(self):
        ordenada = sorted(self.rectangulos, key=lambda x: x.area())
        return ordenada



rectangulo1 = Rectangulo(3, 4)
rectangulo2 = Rectangulo(1, 2)
rectangulo3 = Rectangulo(5, 6)
rectangulos = Rectangulos()
rectangulos.agregar_rectangulo(rectangulo1)
rectangulos.agregar_rectangulo(rectangulo2)
rectangulos.agregar_rectangulo(rectangulo3)
rectangulos = rectangulos.sort()
for i in rectangulos:
    print(i)

"""Escribir una función crear_matriz_triangular(n) que reciba un número entero n y devuelva una matriz triangular inferior de dimensión n x n,
en forma de lista de listas, cuyos elementos no nulos son los números naturales en orden. Por ejemplo, para n = 4,
debe devolver la siguiente matriz:
[[1, 0, 0, 0],
 [2, 3, 0, 0],
 [4, 5, 6, 0],
 [7, 8, 9, 10]]
"""
def crear_matriz_triangular(n):
    matriz = []
    fila = []
    contador = 1
    k = 0
    for i in range(n):
        for j in range(n):
            if j <= k:
                fila.append(contador)
                contador += 1
            else:
                fila.append(0)
        k += 1
        matriz.append(fila)
        fila = []
    return  matriz

print(crear_matriz_triangular(4))

"""Escribir en forma recursiva la función filtrar(cola, funcion) que recibe una cola y una función, y devuelve una nueva cola que contiene
los elementos para los cuales los elementos de la función devuelven True. La cola recibida debe quedar vacía al finalizar la ejecución.
Ejemplo:
cola = Cola([1, 2, 3, 4, 5])
filtrar(cola, es_par)  # Resultado: Cola([2, 4])
"""
#iteratuv0
from cola import Cola
def filtrar(cola, funcion):
    if cola.esta_vacia():
        raise ValueError("Cola Vacia")
    nueva_cola = Cola()
    while not cola.esta_vacia:
        dato = cola.desencolar()
        if funcion(dato):
            nueva_cola.encolar(dato)

    return nueva_cola

#recursivo
def filtrar2(cola, f):
    if cola.esta_vacia():
        return cola
    dato = cola.desencolar()
    cola_filtrada = filtrar2(cola, f)
    if f(dato):
        cola_filtrada.encolar(dato)
    return cola_filtrada

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)
print(cola)
filtrar2(cola, lambda x: x % 2 == 0)
print(cola)

"""

"""


