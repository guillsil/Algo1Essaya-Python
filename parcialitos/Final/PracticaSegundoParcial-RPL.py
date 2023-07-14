"""Escribir una función que reciba una lista de pedidos de un supermercado,
donde cada pedido es un diccionario con el siguiente formato:

{ nombre_producto1: cant1, …, nombre_producto_n: cant_n }

Y escriba un archivo que tenga el resumen de los pedidos con el siguiente formato (sin cabecera):

nombre_producto;cant_total

Siendo cant_total el stock total de ese producto que fue solicitado entre todos los pedidos.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos
deben quedar cerrados."""
def lista_supermercado(lista_pedidos):
    diccionario_resultado = {}
    for pedido in lista_pedidos:
        for producto in pedido:
            if producto in diccionario_resultado:
                diccionario_resultado[producto] += pedido[producto]
            else:
                diccionario_resultado[producto] = pedido[producto]
    return diccionario_resultado
def escribir_archivo(diccionario, ruta_archivo):
    with open(ruta_archivo, "w") as archivo:
        for prducto, cantidad in diccionario.items():
            archivo.write(f"{prducto};{cantidad}\n")

#Prueba
lista_pedidos = [
    {"arroz": 2, "fideos": 1, "pan": 3},
    {"arroz": 1, "fideos": 2, "pan": 1},
    {"arroz": 3, "fideos": 1, "pan": 2},
    {"arroz": 1, "fideos": 1, "pan": 1},
    {"arroz": 2, "fideos": 2, "pan": 2},
    ]
diccionario = lista_supermercado(lista_pedidos)
#escribir_archivo(diccionario, "resumen_pedidos.csv")

"""Se tiene un archivo de texto que contiene un díálogo entre una cantidad de personas
desconocida, de manera que cada línea del archivo tiene este formato

Persona1: una frase de cierta cantidad de palabras
Persona2: otra frase de cierta cantidad de palabras
Persona1: volviendo a hablar
PersonaN: apareciendo con una frase de cierta cantidad de palabras

(asumir que las frases contienen únicamente palabras, no contienen signos de puntuacion,
ni numeros, ni ningun caracter que no sean letras o espacios).

Escribir una funcion que reciba la ruta a un archivo de este tipo y devuelva
cuantas veces dijo cada palabra cada una de las personas involucradas en el díalogo
(es decir, debe devolver un diccionario con el siguiente formato:

{ Persona1: { palabra_1: cant_1, palabra_2: cant_2 }, Persona2: { ... } .. }

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos 
abiertos deben quedar cerrados."""

def contar_palabras(ruta_archivo):
    with open (ruta_archivo, "r") as archivo:
        diccionario = {}
        linea = archivo.readline()
        while linea:
            persona, frase = linea.split(":")
            for palabra in frase.split():
                if persona in diccionario:
                    if palabra in diccionario[persona]:
                        diccionario[persona][palabra] += 1
                    else:
                        diccionario[persona][palabra] = 1
                else:
                    diccionario[persona] = {palabra: 1}
            linea = archivo.readline()
    return diccionario

#Prueba
diccionario = contar_palabras("dialogo.txt")
#print(diccionario)

"""
Implementar la clase CajaFuerte que reproduzca el siguiente comportamiento:

>>> caja = CajaFuerte(9158)
>>> caja.esta_abierta()
False
>>> caja.guardar("pulsera")
Exception: La caja fuerte está cerrada
>>> caja.abrir(1234)
Exception: La clave es inválida
>>> caja.abrir(9158)
>>> caja.esta_abierta()
True
>>> caja.guardar("pulsera")
>>> caja.guardar("reloj de oro")
Exception: No se puede guardar más de una cosa
>>> caja.cerrar()
>>> caja.sacar()
Exception: La caja fuerte está cerrada
>>> caja.abrir(9158)
>>> caja.sacar()
'pulsera'
>>> caja.sacar()
Exception: No hay nada para sacar
"""
class CajaFuerte():
    def __init__(self, clave):
        self.clave = clave
        self.esta_abierta_ = False
        self.objetos = []

    def esta_abierta(self):
        return self.esta_abierta_

    def guardar(self, objeto):
        if self.esta_abierta() == False:
            raise Exception("La caja esta cerrada")
        else:
            if len(self.objetos) >= 1:
                raise Exception("No se puede guardar más de una cosa")
            else:
                self.objetos.append(objeto)

    def abrir(self, clave):
        if clave == self.clave:
            self.esta_abierta_ = True
        else:
            raise Exception("La clave es inválida")

    def cerrar(self):
        self.esta_abierta_ = False

    def sacar(self):
        if self.esta_abierta_ == False:
            raise Exception("La caja fuerte está cerrada")
        elif len(self.objetos) > 0:
            return self.objetos.pop()
        else:
            raise Exception("No hay nada para sacar")

caja = CajaFuerte(9158)
#print(caja.esta_abierta())

"""
Se tiene un diccionario donde cada clave es el título de una canción (cadena), y
cada valor la duración de la canción (en segundos). Se tiene asimismo otro diccionario
donde cada clave es el título de una lista de reproducción (cadena), y cada valor una
lista con títulos de canción que la componen.

Se pide implementar una función que reciba como parámetros ambos diccionarios, y devuelva en forma
de diccionario las duraciones de cada lista de reproducción.

(El diccionario devuelto debe tener como
claves los títulos de lista, y como valor la duración en segundos.)
"""
def duracion_listas(diccionario_canciones, diccionario_listas):
    diccionario_resultado  = {}
    for lista, canciones in diccionario_listas.items():
        duracion = 0
        for cancion in canciones:
            for titulo, duracion_cancion in diccionario_canciones.items():
                if titulo == cancion:
                    duracion += duracion_cancion
        diccionario_resultado[lista] = duracion

    return diccionario_resultado

#Prueba
diccionario_canciones = {
    "cancion1": 100,
    "cancion2": 200,
    "cancion3": 300,
    "cancion4": 400,
    "cancion5": 500,
    "cancion6": 600,
}
diccionario_listas = {
    "lista1": ["cancion1", "cancion2", "cancion3"],
    "lista2": ["cancion4", "cancion5", "cancion6"],
}
diccionario_resultado = duracion_listas(diccionario_canciones, diccionario_listas)
#print(diccionario_resultado)


"""
Escribir una función que reciba el nombre de un archivo, el cual en cada línea tiene un nombre y una
edad, separados por una coma. Devolver en forma de tupla la edad más alta y una lista de nombres de todas
las personas que tienen dicha edad. Se puede abrir y recorrer el archivo sólo una vez y el mismo no entra en memoria.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos
deben quedar cerrados.
"""
import csv
def edad_mas_alta(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        archivo_reader = csv.reader(archivo, delimiter=",")
        edad_mas_alta = 0
        nombres_edad_mas_alta = []
        for nombre , edad in archivo_reader:
            if int(edad) > edad_mas_alta:
                edad_mas_alta = int(edad)
                nombres_edad_mas_alta = [nombre]
            elif int(edad) == edad_mas_alta:
                nombres_edad_mas_alta.append(nombre)
    return (edad_mas_alta, nombres_edad_mas_alta)

#Prueba
edad_mas_alta = edad_mas_alta("personas.csv")
#print(edad_mas_alta)

"""
Escribir una clase Cuenta que tenga el siguiente comportamiento:
c = Cuenta('Pérez')                  
>>> c.acreditar(100, 'Sueldo')       
>>> c.extraer(60, 'Shopping')        
>>> c.saldo()                        
40                                   
>>> print(c)                         
Cuenta de Pérez
>>> d = Cuenta('López')
>>> c.transferir(30, d)
>>> c.saldo()
10
>>> d.saldo()
30
>>> c.movimientos()
[('acreditación', 100, 'Sueldo'), ('extracción', 60, 'Shopping'), ('extracción', 30, 'Cuenta de López')]
>>> d.movimientos()
[('acreditación', 30, 'Cuenta de Pérez')]
>>> d.extraer(100, 'Deudas')
ValueError: Fondos Insuficientes"""

class Cuenta():
    def __init__(self, apellido):
        self.apellido = apellido
        self.dinero = 0
        self.lista_movimientos = []

    def acreditar(self, monto, descripcion):
        self.dinero += monto
        self.lista_movimientos.append(("acreditación", monto, str(descripcion)))

    def extraer(self, monto, descripcion):
        if monto > self.dinero:
            raise ValueError("Fondos Insuficientes")
        else:
            self.dinero -= monto
            self.lista_movimientos.append(("extracción", monto, str(descripcion)))

    def saldo(self):
        return self.dinero

    def __str__(self):
        return "Cuenta de " + self.apellido

    def transferir(self, monto, remitente):
        if monto > self.dinero:
            raise ValueError("Fondos Insuficientes")
        else:
            self.dinero -= monto
            remitente.dinero += monto
            remitente.lista_movimientos.append(("acreditación", monto, str(self)))
            self.lista_movimientos.append(("extracción", monto, str(remitente)))

    def movimientos(self):
        return self.lista_movimientos

c = Cuenta('Pérez')
c.acreditar(100, 'Sueldo')
c.extraer(60, 'Shopping')
print(c.saldo())
print(c)
d = Cuenta('López')
c.transferir(30, d)
print(c.saldo())
print(d.saldo())
print(c.movimientos())












