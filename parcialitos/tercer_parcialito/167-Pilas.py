"""
Se está organizando una fiesta y se conoce la hora de entrada y salida de los N invitados. A cada invitado se le asigna uno de los 3 espacios que hay para estacionar. Cada espacio tiene el ancho de un auto pero el largo de varios, por lo que cada auto que llega bloquea a los que ya estaban previamente. Hacer una función que dada una lista con tuplas (<hora>,<entra/sale>,<invitado>,<espacio>) que están ordenadas por hora, indique si la asignación de espacios es válida. Una asignación es inválida si algún invitado no puede salir a su horario designado porque hay otro auto bloqueándole la salida.

Ejemplo: [(21,ENTRA,"Blas",2), (22,ENTRA,"Ailín",2), (23.5,SALE,"Blas",2), (24,SALE,"Ailín",2)] no es una asignación válida porque el auto de Ailín no deja salir a Blas a horario. En cambio ésta sí es válida: [(21,ENTRA,"Blas",2), (22,ENTRA,"Ailín",2), (23,SALE,"Ailín",2), (23.5,SALE,"Blas",2)].
"""
class Cola:
    def __init__(self):
        self.items = []
    def esta_vacia(self):
        return len(self.items) == 0
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.items.pop(0)
    def ver_frente(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.items[0]
    def __str__(self):
        return str(self.items)
    
class Pila:
    def __init__(self):
        self.items = []
    def esta_vacia(self):
        return len(self.items) == 0
    def apilar(self, x):
        self.items.append(x)
    def desapilar(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.items.pop()
    def ver_tope(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.items[-1]
    def __str__(self):
        return str(self.items)
    
def asignacion_valida(lista_tuplas):
    autos_estacionados = Pila()
    for hora, accion, invitado, espacio in lista_tuplas:
        if accion == "ENTRA":
            autos_estacionados.apilar((hora, invitado, espacio))
        elif accion == "SALE":
            auto_que_sale = autos_estacionados.desapilar()
            if auto_que_sale[1] != invitado:
                return False
    return True


print(asignacion_valida([(21,"ENTRA","Blas",2), (22,"ENTRA","Ailín",2), (23.5,"SALE","Blas",2), (24,"SALE","Ailín",2)]))
print(asignacion_valida([(21,"ENTRA","Blas",2), (22,"ENTRA","Ailín",2), (23,"SALE","Ailín",2), (23.5,"SALE","Blas",2)]))
