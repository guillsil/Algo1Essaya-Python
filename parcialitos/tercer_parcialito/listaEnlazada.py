class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def __str__(self):
        if self.primero is None:
            return "[]"
        else:
            string = "["
            actual = self.primero
            while actual is not None:
                string += str(actual.valor) + ", "
                actual = actual.proximo
            return string[:-2] + "]"
        