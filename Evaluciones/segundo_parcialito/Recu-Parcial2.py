"""Escribir una funcion que reciba por parametro una cadena y devuelva un diccionario cuyas claves sean las
longitudes de cada palabra y  cuyo valor asociado sea una lista de palabras con la longitud indicada.Ejemplo:
>>longitud_palabras("En un lugar de la Mancha de cuyo nombre no quiero acordarme")
{2: ['En', 'un'], 5: ['lugar', 'Mancha'], 6: ['nombre'], 3: ['no', 'que'], 8: ['acordarme']}
"""
def longitud_palabras(cadena):
    diccionario = {}
    palabras = cadena.split()
    for palabra in palabras:
        if len(palabra) not in diccionario:
            diccionario[len(palabra)] = [palabra]
        else:
            diccionario[len(palabra)].append(palabra)
    return diccionario
print(longitud_palabras("En un lugar de la Mancha de cuyo nombre no quiero acordarme"))

"""Escribir una funcion que reciba la ruta de un archivo de lineas con formato nombrer_producto,cantidad_vendida,
siendo nombre_producto una cadena con el nombre de un producto y cantidad_vendida un numero entero positivo con la
cantidad que se vendio. Crear un nuevo archivo con el mismo formato, pero que cada nombre_producto sea único y la 
cantidad_vendida asociada sea la suma de las cantidades de todas las lineas con el mismo nombre_producto."""

def procesar_archivo(ruta):
    try:
        with open(ruta) as archivo:
            productos = {}
            linea = archivo.readline()
            for linea in archivo:
                producto, cantidad = linea.split(",")
                if producto not in productos:
                    productos[producto] = int(cantidad)
                else:
                    productos[producto] += int(cantidad)


        return productos
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

def crear_archivo(productos, ruta):
    try:
        with open(ruta, "w") as archivo:
            for producto, cantidad in productos.items():
                archivo.write(f"{producto},{cantidad}, \n")
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

def main():
    productos = procesar_archivo("productos.txt")
    crear_archivo(productos, "productos_procesados.txt")
main()

"""Escribir la clase Partido, que recibe en el constructor dos cadenas que corresponden a los goles convertidos por
el local y el visitante(en ese orden).Cuenta con los siguientes métodos:
*) cargar_resultado: Recibe dos números enteros , que corresponden a los goles convertidos por el local y el visitante
(en ese orden).
*)obtener_ganador: Devuelve  el nombre del equipo ganador , o None si hubo empate.
*)obtener_perdedor: Devuelve el nombre del equipo perdedor, o None si hubo empate.

Escribir la clase Liga, que tiene los siguientes metodos:
*)cargar_partido: Recibe un objeto de la clase Partido y gurda lo necesario para poder calcular los resultados de los
métodos siguientes.
*)obtener_campeon: Devuelve una cadena con el nombre del equipo campeón, que mas punt tiene . Si hay varios equipos con
la misma cantidad de puntos, devuelve cualquiera de ellos . Se otor ganar 3 puntos, empatar 1 y perder 0.
"""
class Partido:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = 0
        self.goles_visitante = 0
        self.ganador = ""
        self.perdedor = ""

    def cargar_resultado(self, goles_local, goles_visitante):
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        if self.goles_local > self.goles_visitante:
            self.ganador = self.equipo_local
            self.perdedor = self.equipo_visitante
        elif self.goles_local < self.goles_visitante:
            self.ganador = self.equipo_visitante
            self.perdedor = self.equipo_local
        else:
            self.ganador = None
            self.perdedor = None

    def obtener_ganador(self):
        return self.ganador

    def obtener_perdedor(self):
        return self.perdedor

class Liga:
    def __init__(self):
        self.partidos = []

    def cargar_partido(self, partido):
        self.partidos.append(partido)

    def obtener_campeon(self):
        equipos = {}
        for partido in self.partidos:
            if partido.ganador not in equipos:
                equipos[partido.ganador] = 3
            else:
                equipos[partido.ganador] += 3
            if partido.perdedor not in equipos:
                equipos[partido.perdedor] = 0
            if partido.ganador is None and partido.perdedor is None:
                equipos[partido.equipo_local] += 1
                equipos[partido.equipo_visitante] += 1
        maximo = 0
        for equipo, puntos in equipos.items():
            if puntos > maximo:
                maximo = puntos
                campeon = equipo
        return campeon


