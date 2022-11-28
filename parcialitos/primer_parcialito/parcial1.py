"""Escribir una función que dada una matriz representada como una lista de listas, donde cada elemento de
la matriz es una tupla que representa el puntaje de un pais con el formato (<Pais>, <Puntaje>), devuelva una lista
con todos los paises que tengan el mayor puntaje para su columna . En caso de empate , se puede elegir cualquiera .
Por ejemplo para la matriz:
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
matriz = [[("Argentina", 10), ("Brasil", 20), ("Alemania", 30)],
[("Portugal", 20), ("Dinamarca", 30), ("Paraguay", 40)],
[("Croacia", 30), ("Brasil", 40), ("Honduras", 50)]]

"""print(paises_con_mejor_puntaje(matriz))"""


"""Escribir una funcion que le pida al usuario un resultado de un partido hasta que ingreseuno valido. Un resultado 
valido se escribe como <Pais1>:<Pais2>-<Goles1>:<Goles2> donde el país es una cadena y goles es un número positivo.
La función debe devolver los cuatro campos del resultado. En caso que el formato sea inválido , se le deberá mostrar
al usuario un mensaje de error y volver a preguntarle . 
Ejemplo:
"Argentina:Brasil-2:1" es válido
"Argentina:Brasil-2:1:3" es inválido
"""
def pedir_resultado():
    resultado = input("Ingrese el resultado: ")
    while not resultado_valido(resultado):
        print("El resultado no es válido.")
        resultado = input("Ingrese el resultado: ")
    return resultado

def resultado_valido(resultado):
    """Devuelve True si el resultado es válido, False en caso contrario"""
    resultado = resultado.split("-")
    if len(resultado) != 2:
        return False
    goles = resultado[1].split(":")
    if len(goles) != 2:
        return False
    if not goles[0].isdigit() or not goles[1].isdigit():
        return False
    equipos = resultado[0].split(":")
    if len(equipos) != 2:
        return False
    if not equipos[0].isalpha() or not equipos[1].isalpha():
        return False
    return True
"""print(pedir_resultado())"""

"""Escribir una funcion censurar que, dado un texto y una lista de palabras a censurar , devuelva un nuevo texto con 
todas las palabras censuradas (considerando todad las apariciones) reemplazadas por el caracter *.La función 
 debe cencurar ignorando las mayusculas y minusculas . Ejemplo:
 censurar("Hola mundo", ["H",  "a"]) -> "*ol* mundo"
 """
def censurar(texto, lista_palabras):
    cadena = ""
    for c in texto:
        if c in lista_palabras:
            cadena += "*"
        else:
            cadena += c
    return cadena
print(censurar("Hola mundo", ["H", "a"]))



