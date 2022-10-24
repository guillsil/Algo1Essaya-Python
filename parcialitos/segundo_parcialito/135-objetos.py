"""Se pide implementar una clase Semaforo con tres luces (roja, amarilla y verde) y el siguiente comportamiento:
Al instanciar la clase se debe ver la luz roja prendida.​
Debe tener un metodo siguiente para apagar la luz actual y encender la siguiente (el orden de encendido de las luces es
roja->amarilla->verde->roja->amarilla->...)
Debe tener un metodo apagar que apague el semaforo. En un semaforo apagado todas las luces estan apagadas y no se
puede encender ninguna. Si se intenta usar el metodo siguiente mientras el semaforo esta apagado se debe lanzar una
excepcion del tipo ValueError.
Debe tener un metodo encender que encienda el semaforo. Al encender el semaforo el estado de las luces debe ser el
mismo que tenia antes de apagarlo.
Al imprimir una instancia de la clase semaforo, debe mostrar qué luz esta prendida. Si el semaforo esta apagado,
debe mostrar que esta apagado.
La representacion interna de la clase es a criterio pero debe ser acorde al comportamiento y no agregar complejidad."""
class Semafaro:
    def __init__(self):
        self.rojo = True
        self.amarillo = False
        self.verde = False
        self.apagado = False
    def siguiente(self):
        if self.apagado:
            raise ValueError
        if self.rojo:
            self.rojo = False
            self.amarillo = True
        elif self.amarillo:
            self.amarillo = False
            self.verde = True
        elif self.verde:
            self.verde = False
            self.rojo = True
    def apagar(self):
        self.apagado = True
        self.rojo = False
        self.amarillo = False
        self.verde = False
    def encender(self):
        self.apagado = False
    def __str__(self):
        if self.apagado:
            return "Apagado"
        elif self.rojo:
            return "Rojo"
        elif self.amarillo:
            return "Amarillo"
        elif self.verde:
            return "Verde"
