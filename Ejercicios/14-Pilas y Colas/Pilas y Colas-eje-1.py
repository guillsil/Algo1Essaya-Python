"""Escribir una clase TorreDeControl que modele el trabajo de una torre de control de
un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen
prioridad sobre los que están esperando para despegar. La clase debe funcionar conforme al
siguiente ejemplo:
>> torre = TorreDeControl()
>> torre.nuevo_arribo('AR156')
>> torre.nueva_partida('KLM1267')
>> torre.nuevo_arribo('AR32')
>> torre.ver_estado()
Vuelos esperando para aterrizar: AR156, AR32
Vuelos esperando para despegar: KLM1267
>> torre.asignar_pista()
El vuelo AR156 aterrizó con éxito.
>> torre.asignar_pista()
El vuelo AR32 aterrizó con éxito.
>> torre.asignar_pista()
El vuelo KLM1267 despegó con éxito.
>> torre.asignar_pista()
No hay vuelos en espera."""

class TorreDeControl:
    def __init__(self):
        self.arribos = []
        self.partidas = []
    def nuevo_arribo(self, vuelo):
        self.arribos.append(vuelo)
    def nueva_partida(self, vuelo):
        self.partidas.append(vuelo)
    def ver_estado(self):
        print("Vuelos esperando para aterrizar:", ", ".join(self.arribos))
        print("Vuelos esperando para despegar:", ", ".join(self.partidas))
    def asignar_pista(self):
        if self.arribos:
            print("El vuelo", self.arribos.pop(0), "aterrizó con éxito.")
        elif self.partidas:
            print("El vuelo", self.partidas.pop(0), "despegó con éxito.")
        else:
            print("No hay vuelos en espera.")

torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.ver_estado()
