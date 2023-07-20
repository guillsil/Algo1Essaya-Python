"""Escribir una clase Caja para representar cuánto dinero hay en una caja de un negocio, desglosado por tipo de billete
(por ejemplo, en el quiosco de la esquina hay 6 billetes de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos).
Las denominaciones permitidas son 1, 2, 5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el
siguiente ejemplo:
#>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
#>>> c = Caja({500: 6, 100: 7, 2: 4})
#>>> str(c)
'{500: 6, 100: 7, 2: 4}'
#>>> c.total()
3708
#>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
#>>> c.agregar({50: 2, 2: 1})
#>>> str(c)
'{500: 6, 100: 7, 50: 2, 2: 5}'
#>>> c.total()
3810
#>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
#>>> c.quitar({50: 2, 100: 1})
200
#>>> str(c)
'{500: 6, 100: 6, 2: 5}'
#>>> c.total()
3610Nota: Si al quitar no hay suficientes billetes de alguna denominación, debe cancelarse toda la transacción y no
retirar ningún billete (ver anteúltima llamada a quitar del ejemplo)"""
class Caja:
    def __init__(self, diccionario):
        self.diccionario = diccionario
        self.lista = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        for i in diccionario:
            if i not in self.lista:
                raise ValueError('Denominación "{}" no permitida'.format(i))
    def __str__(self):
        return str(self.diccionario)
    def total(self):
        total = 0
        for i in self.diccionario:
            total += i * self.diccionario[i]
        return total
    def agregar(self, diccionario):
        for i in diccionario:
            if i not in self.lista:
                raise ValueError('Denominación "{}" no permitida'.format(i))
            else:
                if i in self.diccionario:
                    self.diccionario[i] += diccionario[i]
                else:
                    self.diccionario[i] = diccionario[i]
    def quitar(self, diccionario):
        for i in diccionario:
            if i not in self.diccionario:
                raise ValueError('Denominación "{}" no permitida'.format(i))
            else:
                if diccionario[i] > self.diccionario[i]:
                    raise ValueError('No hay suficientes billetes de denominación "{}"'.format(i))
                else:
                    self.diccionario[i] -= diccionario[i]
                    return i * diccionario[i]


