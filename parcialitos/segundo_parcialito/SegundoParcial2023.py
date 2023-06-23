"""1. Se solicita crear una función str, ruta _ gal ida: str) que recibe la ruta a un archivo
CSV con información sobre los proyectos en los que los empleados dc una empresa están trabajando, con formato
La función debe escribir un nuevo archivo CSV dado por el parametro de ruta _ gal ida, con el listado de empleados por proyecto. cron
formato , {emplead02} , ....
Por ejemplo, a partir del archivo de la izquierda, deberá generarse el archivo de
la derecha:
Javier , Backoffice
Mati S, Fintech
Nacho , API
C, API
Mauro , Backoffice
Backoff ice->Javier , Mauro
Fintech->Mati S"""
import csv

#1
import csv

def empleadosPorProyectos(ruta_entrada, ruta_salida):
    proyectos = {}
    with open(ruta_entrada, "r") as archivo_entrada, open(ruta_salida, "w") as archivo_salida:
        entrada = csv.reader(archivo_entrada)
        salida = csv.writer(archivo_salida)
        for linea in entrada:
            if len(linea) != 2:
                continue
            empleado, proyecto = linea[0], linea[1]
            if proyecto not in proyectos:
                proyectos[proyecto] = [empleado]
            proyectos[proyecto].append(empleado)
        for proyecto, empleados in proyectos.items():
            salida.writerow([proyecto, *empleados])

    
empleadosPorProyectos("empleados.csv", "empleadosPorProyectos.csv")

#2
"""2. Se pide implementar una función maximos_donantes(donaciones), que recibe una lista de tuplas las cuales
representan una donación que realizó un determinado usuario de MercadoPago al Club Atlético Independiente, e imprima los nombres de
aquellos que hayan donado la mayor cantidad de dinero. Ejemplos:
("MatiChurches" ,5000), ("FabiDoman" ,100), ("EIKun" ,5), ("RodriS" ,4000)) )
>>> , 1000) ,
Marinos donantes: RodriS , MatiChurches
("Galperin" ,1000000)) )
>>> [("RojoPasion" , 100) ,
Maximos donantes: Galperin"""
def regitroDonaciones(donaciones):
    donadores = {}
    for donacion in donaciones:
        donador, monto = donacion
        if donador not in donadores:
            donadores[donador] = monto
        donadores[donador] += monto
    return donadores
def maximos_donantes(donadores):
    maxDonadores = {}
    maxMonto = 0
    for donador, monto in donadores.items():
        if monto > maxMonto:
            maxMonto = monto
            maxDonadores = {donador}
        elif monto == maxMonto:
            maxDonadores.add(donador)
    return maxDonadores
donaciones = [("MatiChurches" ,5000), ("FabiDoman" ,100), ("EIKun" ,5), ("RodriS" ,5000)]
donadores = regitroDonaciones(donaciones)
maxDonadores = maximos_donantes(donadores)
print(f"Maximos donantes: {', '.join(maxDonadores)}")

#3
"""3. Para un nuevo sistema de facultad, se pide ilnp ementar a case ateria, que necesi a e un nom rc y una can 1
para
ser creada. Una Materia ademas cuenta con una nota (inicialmente sin asignar), y una lista de correlativas (las materias que necesitan
estar aprobadas antes de poder cursar esa materia). Se busca que la clase tenga los siguientes métodos:
• imprimir _ informacion(self): debe imprimir el nombre, la descripción, la cantidad de créditos de la materia, y su estado (aprQF
bada/no aprobada).
• bool: retorna True en caso de estar aprobada (se aprueba con 4)
• nota: int): se le asigna una nota a la materia. La nota tiene que estar entre los valores 0 y 10, de 10 contrario,
debe lanzarse una excepcion.
correlativa: Materia): agrega la correlativa pasada por parámetro a la materia.
• puede_cursarse (self) bool: debe retornar True en caso de que se cumplan los requerimientos para poder cursarla
"""
class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        self.correlativas = []
        self.nota = None
    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}, Creditos: {self.creditos}, Nota: {self.nota}")
    def esta_aprobada(self):
        return self.nota >= 4
    def asignar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        self.nota = nota
    def agregar_correlativa(self, correlativa):
        self.correlativas.append(correlativa)
    def puede_cursarse(self):
        for correlativa in self.correlativas:
            if not correlativa.esta_aprobada():
                return False
        return True
    
    