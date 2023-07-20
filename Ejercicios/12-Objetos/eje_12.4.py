"""Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
#>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
#>>> c = Caja({500: 6, 100: 7, 2: 4})
#>>> str(c)
'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
#>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
#>>> c.agregar({50: 2, 2: 1})
#>>> str(c)
'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
#>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
#>>> c.quitar({50: 2, 100: 1})
200
#>>> str(c)
'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'"""
class Caja:
    def __init__(self, diccionario):
        self.diccionario = diccionario
        self.denominaciones = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        for i in self.diccionario:
            if i not in self.denominaciones:
                raise ValueError("Denominación no permitida")
    def __str__(self):
        return f"Caja {self.diccionario} total: {self.total()} pesos"
    def agregar(self, diccionario):
        for i in diccionario:
            if i not in self.denominaciones:
                raise ValueError("Denominación no permitida")
            else:
                if i in self.diccionario:
                    self.diccionario[i] += diccionario[i]
                else:
                    self.diccionario[i] = diccionario[i]
    def quitar(self, diccionario):
        for i in diccionario:
            if i not in self.denominaciones:
                raise ValueError("Denominación no permitida")
            else:
                if i in self.diccionario:
                    if self.diccionario[i] < diccionario[i]:
                        raise ValueError("No hay suficientes billetes de denominación")
                    else:
                        self.diccionario[i] -= diccionario[i]
                else:
                    raise ValueError("No hay suficientes billetes de denominación")
        return self.total()
    def total(self):
        total = 0
        for i in self.diccionario:
            total += i * self.diccionario[i]
        return total
"""probar el objeto"""
caja1 = Caja({500: 6, 100: 7, 2: 4})
print(caja1.__str__())
print(caja1.agregar({50: 2, 2: 1}))
print(caja1.__str__())
print(caja1.quitar({50: 2, 100: 1}))
print(caja1.__str__())




