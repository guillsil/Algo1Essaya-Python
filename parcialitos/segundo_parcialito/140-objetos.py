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
class CajaFuerte:
    def __init__(self, clave):
        self.clave = clave
        self.abierta = False
        self.items = None
    def esta_abierta(self):
        return self.abierta
    def abrir(self, clave):
        while True:
            if clave == self.clave:
                self.abierta = True
                break
            else:
                raise Exception("La clave es inválida")
    def cerrar(self):
        self.abierta = False
    def guardar(self, cosa):
        if self.abierta == False:
            raise Exception("La caja fuerte está cerrada")
        if self.items == None:
            self.items = cosa
        else:
            raise Exception("No se puede guardar más de una cosa")
    def sacar(self):
        if self.abierta == False:
            raise Exception("La caja fuerte está cerrada")
        if self.items == None:
            raise Exception("No hay nada para sacar")
        else:
            item = self.items
            self.items = None
            return item
        
        
