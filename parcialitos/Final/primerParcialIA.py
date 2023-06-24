"""    Funciones y ciclos:
    Ejercicio 1: Escribe una función llamada multiplos que tome un número y un límite como argumentos y devuelva una lista con todos los múltiplos del número hasta el límite.

    Interacción y validación de entrada:
    Ejercicio 2: Escribe una función llamada ingresar_edad que solicite al usuario ingresar su edad. La función debe asegurarse de que el valor ingresado sea un número entero positivo.

    Listas y búsqueda:
    Ejercicio 3: Escribe una función llamada buscar_elemento_lista que tome una lista y un elemento como argumentos, y devuelva la posición (índice) del elemento en la lista. Si el elemento no está presente, la función debe devolver -1.

    Cadenas y manipulación de texto:
    Ejercicio 4: Escribe una función llamada contar_vocales que tome una cadena como argumento y devuelva la cantidad de vocales que contiene.

    Archivos y procesamiento de texto:
    Ejercicio 5: Escribe un programa que lea un archivo de texto y cuente la cantidad de palabras distintas que aparecen en el texto.

    Ciclos y manipulación de listas:                                    
    Ejercicio 6: Escribe una función llamada eliminar_repetidos que tome una lista y elimine los elementos duplicados, dejando únicamente una aparición de cada elemento en la lista."""

#1
def multiplos(numero, limite):
    lista = []
    for i in range(1, limite + 1):
        if i % numero == 0:
            lista.append(i)
    return lista
print(multiplos(3, 20))
#2
def ingresar_edad():
    while True:
        edad = input("Ingrese su edad: ")
        if edad.isdigit() and int(edad) > 0:
            return int(edad)
        print("Edad inválida.")
print(ingresar_edad())

#3
def buscar_elemento_lista(lista, argumento):
    for i in range(len(lista)):
        if lista[i] == argumento:
            return i
    return -1
print(buscar_elemento_lista([1, 2, 3, 4, 5], 3))

#3 parecido al 3 pero implemetando busqueda binaria
def buscar_elemento_lista_binaria(lista, argumento):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == argumento:
            return medio
        elif lista[medio] > argumento:
            fin = medio - 1
        else:
            inicio = medio + 1
    return -1
print(buscar_elemento_lista_binaria([1, 2, 3, 4, 5], 3))
#4
VOCALES = "aeiou"
def contar_vocales(cadena):
    contador = 0
    for caracter in cadena:
        if caracter in VOCALES:
            contador += 1
    return contador
print(contar_vocales("hola mundo"))
#5
def contar_palabras_distintas(archivo):
    with open(archivo, "r") as archivo:
        linea = archivo.readline()
        palabras = set()
        for palabra in linea.split():
            if palabra in palabras:
                continue
            palabras.add(palabra)
        return len(palabras)
    
print(contar_palabras_distintas("archivo.txt"))

#6
def eliminar_repetidos(lista):
    lista_nueva = []
    for elemento in lista:
        if elemento in lista_nueva:
            continue
        lista_nueva.append(elemento)
    return lista_nueva

