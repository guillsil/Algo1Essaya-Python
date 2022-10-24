"""Escribir la clase Pelea, que recibe en el constructor dos cadenas que corresponden al nombre del retador y
el defensor (en ese orden). Además, tiene los siguientes métodos:
cargar_resultado: Recibe dos números enteros, que corresponden a los puntos asignados al retador y al defensor
(en ese orden).obtener_ganador: Devuelve el nombre del participante ganador, o la cadena "TIE" sí hubo un empate.
Escribir la clase HistorialDePeleas, que tiene los siguientes métodos:
cargar_pelea: Recibe un objeto de clase Pelea (de ella puede guardar solo los datos necesarios)
obtener_record: Devuelve una cadena con el nombre del competidor que más peleas ganó en toda la historia y cuantas fueron.
Si hay varios peleadores que tengan la misma cantidad de peleas ganadas, devolver alguno de todos. Este método debe ser
lo más eficiente posible. En la clase Pelea validar los parámetros recibidos, y lanzar la excepción que corresponda
si no cumplen las condiciones.
"""
class Pelea:
    def __init__(self, redactor, defensor):
        """validar los parámetros recibidos, y lanzar la excepción que corresponda
        si no cumplen las condiciones."""
        if redactor == defensor:
            raise Exception("No se puede pelear contra uno mismo")
        if not isinstance(redactor, str) or not isinstance(defensor, str):
            raise Exception("Los nombres deben ser cadenas de caracteres")
        self.redactor = redactor
        self.defensor = defensor
        self.puntos_redactor = 0
        self.puntos_defensor = 0
    def cargar_resultado(self, puntos_redactor, puntos_defensor):
        self.puntos_redactor = puntos_redactor
        self.puntos_defensor = puntos_defensor
    def obtener_ganador(self):
        if self.puntos_redactor > self.puntos_defensor:
            return self.redactor
        elif self.puntos_redactor < self.puntos_defensor:
            return self.defensor
        else:
            return "TIE"
class HistorialDePeleas: # No se si esta bien
    def __init__(self):
        self.historial = []
    def cargar_pelea(self, pelea):
        self.historial.append(pelea)
    def obtener_record(self):
        record = {}
        for pelea in self.historial:
            if pelea.obtener_ganador() in record:
                record[pelea.obtener_ganador()] += 1
            else:
                record[pelea.obtener_ganador()] = 1
        maximo = 0
        ganador = ""
        for nombre, cantidad in record.items():
            if cantidad > maximo:
                maximo = cantidad
                ganador = nombre
        return ganador, maximo
pelea1 = Pelea("Juan", "Pedro")
pelea1.cargar_resultado(10, 5)
pelea1.obtener_ganador()
pelea2 = Pelea("Juan", "Pedro")
pelea2.cargar_resultado(5, 10)
pelea2.obtener_ganador()
pelea3 = Pelea("Juan", "Pedro")
pelea3.cargar_resultado(5, 5)
pelea3.obtener_ganador()
pelea4 = Pelea("Juan", "Pedro")
pelea4.cargar_resultado(10, 5)
pelea4.obtener_ganador()

historial = HistorialDePeleas()
historial.cargar_pelea(pelea1)
historial.cargar_pelea(pelea2)
historial.cargar_pelea(pelea3)
historial.cargar_pelea(pelea4)
print(historial.obtener_record())






