#Segundo Parcialito
#1)
"""Implementar la clase Partido que reproduzca el siguiente comportamiento:
>>partido =  Partido ("Argentina", "Polonia")
>>partido .registrar_gol(Argentina", "Messi")
>>print(partido)
Argentina 1 (Messi)
>>partido.registrar_gol("Argentina", "Martinez")
>>partido.registrar_gol("Argetina", "Messi")
>>partido.registrar_gol("Polonia", "Kuba")
>>partido.registrar_gol("Mexico", "Funes Mori")
ValueError: El equipo Mexico no juega el partido
Argentina 3 (Messi, Martinez, Messi)
Polonia 1 (Kuba)
"""
class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles1 = 0
        self.goles2 = 0
        self.goleadores1 = []
        self.goleadores2 = []
    def registrar_gol(self, equipo, jugador):
        if equipo == self.equipo1:
            self.goles1 += 1
            self.goleadores1.append(jugador)
        elif equipo == self.equipo2:
            self.goles2 += 1
            self.goleadores2.append(jugador)
        else:
            raise ValueError("El equipo {} no juega el partido".format(equipo))
    def __str__(self):
        return "{} {} ({})\n{} {} ({})".format(self.equipo1, self.goles1, ", ".join(self.goles1_lista), self.equipo2,
                                               self.goles2, ", ".join(self.goles2_lista))

#2)
"""Dado un archivo que Registra las ventas de entradas de los partidos del mundial en formato  csv el cual contine  
las columnas nombre_comprador, equipo1, equipo2, escribir una función que devuelva al equipo mas popular, del mundial 
según la cantidad de ventas. Cada filadel archivo corresponde a una entrada vendida y el mismo no posee encabesado 
.Si hay más de un quipo con la mayor  cantidad de ventas , debe devolverse cualquiera de ellos. 
"""
def equipo_mas_popular(archivo):
    equipos = {}
    with open(archivo) as f:
        for linea in f:
            equipo = linea.split(",")
            if equipo[1] in equipos:
                equipos[equipo[1]] += 1
            else:
                equipos[equipo[1]] = 1
            if equipo[2] in equipos:
                equipos[equipo[2]] += 1
            else:
                equipos[equipo[2]] = 1

    maximo = 0
    max_vendedor = ""
    for equipo, ventas in equipos.items():
        if ventas > maximo:
            maximo = ventas
            max_vendedor = equipo
    return max_vendedor
print(equipo_mas_popular("entradas.csv"))

#3)
"""Escribir una función que devuelva un diccionario de países , cuyos valores sean una lista de todos los equipos de todos los 
equipos a los cuales pertenecen sus jugadores(sin repetirlos). La función recibe un diccionario que tiene como claves jugadores y 
como valores su país al cual representa, y otro diccionario que tiene como claves equipos y como valores una lista de jugadores .Por 
ejemplo , para , los siguientes diccionarios (se puede asumir que todos los jugadores existen en el diccionario):
diccionario1 = {
    "Messi": "Argentina",
    "Neymar": "Brasil",
    "Paredes": "Argentina",
    "Otamendi": "Argentina",
}
diccionario2 = {
    "PSG" : ["Neymar", "Paredes", "Messi"],
    "Benfica" : ["Otamendi""],
}
{
    "PSG" : ["Neymar", "Paredes", "Messi"],
    "Benfica" : ["Otamendi""],
}
Debe devolverse el siguiente diccionario.No es necesario que los elemetos de las listas tengan un orden particular.
{ 
    "Argentina" : ["PSG", "Benfica"],
    "Brasil" : ["PSG"],
}
"""
diccionario1 = {
    "Messi": "Argentina",
    "Neymar": "Brasil",
    "Paredes": "Argentina",
    "Otamendi": "Argentina",
}
diccionario2 = {
    "PSG" : ["Neymar", "Paredes", "Messi"],
    "Benfica" : ["Otamendi"]
}
def paises_con_equipos(jugador_pais, equipo_jugadores):
    resultado = {}
    for equipo, jugadores in equipo_jugadores.items():
        for jugador in jugadores:
            pais = jugador_pais[jugador]
            if pais in resultado:
                #resultado es un diccionario, resultado[pais] es una lista
                if equipo not in resultado[pais]:
                    resultado[pais].append(equipo)
            else:
                resultado[pais] = [equipo]
    return resultado
print(paises_con_equipos(diccionario1, diccionario2))


