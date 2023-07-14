"""
1)Escribir una funcion imprimir_notables que reciba una secuencia de movimiento de la forma
<personaje>,<movimiento> y un numero k. La funcion debe imprimir por pantalla todos los movimientos "notables" de cada
personaje y cuántas veces se usaron .
Se dice que un Movimiento es "notable" si el personaje lo utilizó más de k veces durante la partida . Se deben mostrar
todos los movimientos notables . Se puede mostrar los movimientoss en cualquier orden.Ejemplo:
>> movimientos = [("pikachu", "impactrueno"), ("Charizard", "Lanzallamas"), ("Charizard", "Lanzallamas"),
("pikachu", "Ataque Rapído"), ("pikachu", "Ataque Rapído", ("Charizard", "Lanzallamas"))]
>> imprimir_notable(movimientos, 1)
Charizard - Lanzallamas (3)
Pikachu - Ataque Rapido (2)
"""
def imprimir_notables(movimientos, k):
    movimiento_notables = {}
    for personaje, movimiento in movimientos:
        if personaje not  in movimiento_notables:
            movimiento_notables[personaje] = {movimiento: 1}
        else:
            movimiento_notables[personaje][movimiento] = movimiento_notables[personaje].get(movimiento, 0) + 1
            #get() devuelve el valor del elemento con la clave especificada. Si la clave no existe, devuelve el valor

    for personaje, movimientos in movimiento_notables.items():
        for movimiento, cantidad in movimientos.items():
            if cantidad > k:
                print(f"{personaje} - {movimiento} ({cantidad})")

movimientos = [("pikachu", "impactrueno"), ("Charizard", "Lanzallamas"), ("Charizard", "Lanzallamas"),
               ("pikachu", "Ataque Rapido"), ("pikachu", "Ataque Rapido"), ("Charizard", "Lanzallamas")]
imprimir_notables(movimientos, 1)

"""Se cuenta con un  archivo en formato csv que guarda información de pasajes de avión, respetando la siguiente
estructura: fecha, destino, precio. Escribir una función que dada la ruta del archivo, devuelva un diccionario cuyas 
claves sean cada uno de los destinos, y el valor asociado a cada clave una tupla (fecha, precio) con el pasaje más barato
 para el destino. Al finalizar la ejecucion de la funcón (haya ocurrido un error o no), todos los archivos abiertos deben 
quedar cerrados"""
import csv 

def obtener_menor_precio(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        archivo_csv = csv.reader(archivo)
        pasajes = {}
        for fecha, destino, precio in archivo_csv:
            if destino not in pasajes:
                pasajes[destino] = (fecha, precio)
            else:
                if precio < pasajes[destino][1]:
                    pasajes[destino] = (fecha, precio)
        return pasajes
    
#print(obtener_menor_precio("pasajes.csv"))

"""
3. Se Pide inplementar una clase CalendarioMes con los siguientes métodos:
• __inlt__ (dias: int): toma como parámetro un entero que representa el número de días que tiene el mes (entre 28 Y 31). Debe lanzar una excepción si no es un día válido.
• agregar_evento(dia: int, evento: str): torna como parámetro un día (número entero) Y el nombre de un evento
(cadena) y lo almacena en el calendario. Debe lanzar una excepción si no es un día válido•
• eliminar_evento(int, evento: str): toma como parámetro un día y el nombre de un evento y l0 elimina del
calendario. Debe lanzar una excepción si no existe un evento con ese nombre en ese día o si el día es inválido.
• obtener_eventos_dia(dia: int) -> list[str): toma como parámetro un día Y devuelve una lista con los eventos
programados para ese día, o la lista vacía si no hay eventos en día. Debe lanzar una excepción si no es un válido
"""
class CalendarioMes():
    def __init__(self, dias):
        if dias < 28 or dias > 31:
            raise Exception("No es un dia valido")
        self.dias = dias
        self.calendario = {}

    def agregar_evento(self, dia, evento):
        if dia < 1 or dia > self.dias:
            raise Exception("No es un dia valido")
        if dia not in self.calendario:
            self.calendario[dia] = [evento]
        else:
            self.calendario[dia].append(evento)

    def eliminar_evento(self, dia, evento):
        if evento not in self.calendario[dia]:
            raise Exception("No existe un evento con ese nombre en ese dia")
        if dia < 1 or dia > self.dias:
            raise Exception("No es un dia Valido")
        if dia in self.calendario:
            self.calendario[dia].remove(evento)
        
    def obtener_eventos_dia(self, dia):
        if dia < 1 or dia > self.dias:
            raise Exception("No es un dia Valido")
        if dia in self.calendario:
            return self.calendario[dia]
        else:
            return []
        
calendario = CalendarioMes(30)
calendario.agregar_evento(1, "Cumpleaños")
calendario.agregar_evento(5, "Confirmacion")  
calendario.agregar_evento(1, "Bautismo")

print(calendario.obtener_eventos_dia(7))






             


        
            
