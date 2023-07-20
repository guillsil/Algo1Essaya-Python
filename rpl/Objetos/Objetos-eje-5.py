"""Crear las clases Materia(codigo, nombre, creditos) y Carrera(materias), que se comporten según el
siguiente ejemplo:
#>>> analisis2 = Materia("61.03", "Análisis 2", 8)
#>>> fisica2 = Materia("62.01", "Física 2", 8)
#>>> algo1 = Materia("75.40", "Algoritmos 1", 6)
#>>> c = Carrera([analisis2, fisica2, algo1])
#>>> c.materias_aprobadas()
[]
#>>> c.promedio()
ValueError: No hay materias aprobadas
#>>> c.creditos_obtenidos()
0
#>>> c.aprobar("95.14", 7)
ValueError: La materia 95.14 no es parte del plan de estudios
#>>> c.aprobar("75.40", 10)
#>>> c.aprobar("62.01", 7)
#>>> c.materias_aprobadas()
['75.40 Algoritmos 1 (10)', '62.01 Física 2 (7)']
#>>> c.creditos_obtenidos()
14
#>>> c.promedio()
8.5
Nota: El formato de la cadena para las materias aprobadas es {codigo} {materia} ({nota})
Nota 2: Se recomienda leer la sección 14.5 Composición de objetos del apunte teórico de la materia"""
class Materia:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
class Carrera:
    def __init__(self, materias):
        self.materias = materias
        self.materias_aprobadas = []
        self.creditos_obtenidos = 0
        self.promedio = 0
    def aprobar(self, codigo, nota):
        for i in self.materias:
            if i.codigo == codigo:
                self.materias_aprobadas.append('{} {} ({})'.format(i.codigo, i.nombre, nota))
                self.creditos_obtenidos += i.creditos
                self.promedio +=  nota
                return
        raise ValueError('La materia {} no es parte del plan de estudios'.format(codigo))
    def materias_aprobadas(self):
        return self.materias_aprobadas
    def creditos_obtenidos(self):
        return self.creditos_obtenidos
    def promedio(self):
        return self.promedio / len(self.materias_aprobadas)
