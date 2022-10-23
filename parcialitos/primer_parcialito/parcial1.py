"""Escribir una función que dada una matriz representada como una lista de listas, donde cada elemento de la matriz es una
tupla que representa el puntaje de un pais con el formato (<Pais>, <Puntaje>), devuelva una lista con todos los paises que
tengan el mayor puntaje para su columna . En caso de empate , se puede elegir cualquiera . Por ejemplo para la matriz:
[[(Argentina, 10), (Brasil, 20), (Alemania, 30)],
[(Portugal, 20), (Dinamarca, 30), (Paraguay, 40)],
[(Croacia, 30), (Brasil, 40), (Honduras, 50)]]
"""
def paises_con_mejor_puntaje(matriz):
    lista_paises = []
    for i in range(len(matriz[0])):
        puntaje_maximo = 0
        for j in range(len(matriz)):
            if matriz[j][i][1] > puntaje_maximo:
                puntaje_maximo = matriz[j][i][1]
        for j in range(len(matriz)):
            if matriz[j][i][1] == puntaje_maximo:
                lista_paises.append(matriz[j][i][0])
    return lista_paises

"""Escribir una funcion que le pida al usuario un resultado de un partido hasta que ingreseuno valido. Un resultado valido se 
escribe como <Pais1>:<Pais2>-<Goles1>:<Goles2> donde el país es una cadena y goles es un número positivo .La función debe 
devolver los cuatro campos del resultado. En caso que el formato sea inválido , se le deberá mostrar al usuario un mensaje
de error y volver a preguntarle . Ejemploa:
"Argentina:Brasil-2:1" es válido
"Argentina:Brasil-2:1:3" es inválido
"""
def pedir_resultado():
    resultado = input("Ingrese el resultado del partido: ")
    while not resultado_valido(resultado):
        print("El resultado ingresado no es válido.")
        resultado = input("Ingrese el resultado del partido: ")
    return resultado

def resultado_valido(resultado):
    resultado1 = resultado.split("-")
    resultado2 = resultado1[0].split(":")
    resultado3 = resultado1[1].split(":")
    if len(resultado1) != 2:
        return False
    if len(resultado2) != 2:
        return False
    if len(resultado3) != 2:
        return False
    if not resultado2[0].isalpha() or not resultado2[1].isalpha():
        return False
    if not resultado3[0].isdigit() or not resultado3[1].isdigit():
        return False
    return True

"""Escribir una funcion censurar que, dado un texto y una lista de palabras a censurar , devuelva un nuevo texto con 
todas las palabras censuradas (considerando todad las apariciones) reemplazadas por el caracter *.La función 
 debe cencurar ignorando las mayusculas y minusculas . Ejemplo:
 censurar("Hola mundo", ["H",  "a"]) -> "*ol* mundo"
 """
def censurar(texto, lista_palabras):
    texto = texto.split()
    for i in range(len(texto)):
        for j in range(len(lista_palabras)):
            if texto[i].lower() == lista_palabras[j].lower():
                texto[i] = "*" * len(texto[i])
    return " ".join(texto)
