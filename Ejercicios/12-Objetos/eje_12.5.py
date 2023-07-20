"""Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo::
#>>> analisis2 = Materia("61.03", "Análisis 2", 8)
#>>> fisica2 = Materia("62.01", "Física 2", 8)
#>>> algo1 = Materia("75.40", "Algoritmos 1", 6)
#>>> c = Carrera([analisis2, fisica2, algo1])
#>>> str(c)
Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
#>>> c.aprobar("95.14", 7)
ValueError: La materia 75.14 no es parte del plan de estudios
#>>> c.aprobar("75.40", 10)
#>>> c.aprobar("62.01", 7)
#>>> str(c)
Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
75.40 Algoritmos 1 (10)
62.01 Física 2 (7)"""
class Materia:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
    def __str__(self):
        return f"{self.codigo} {self.nombre} ({self.creditos})"

class Carrera:
    def __init__(self, lista):
        self.lista = lista
        self.creditos = 0
        self.promedio = 0
        self.materias = []
    def __str__(self):
        return f"Créditos: {self.creditos} | Promedio: {self.promedio} | Materias aprobadas: {self.materias}"
    def aprobar(self, codigo, nota):
        for i in self.lista:
            if i.codigo == codigo:
                self.creditos += i.creditos
                self.promedio = (self.promedio + nota) / 2
                self.materias.append(i.__str__())
            else:
                raise ValueError("La materia no es parte del plan de estudios")
materia1 = Materia("61.03", "Análisis 2", 8)
materia2 = Materia("62.01", "Física 2", 8)
materia3 = Materia("75.40", "Algoritmos 1", 6)
carrera = Carrera([materia1, materia2, materia3])
carrera.aprobar("75.40", 10)
carrera.aprobar("62.01", 7)
carrera.aprobar("61.03", 8)
print(carrera.__str__())

