"""Se está organizando una fiesta y se conoce la hora de entrada y salida de los N invitados. A cada invitado
se le asigna uno de los 3 espacios que hay para estacionar. Cada espacio tiene el ancho de un auto pero el
largo de varios, por lo que cada auto que llega bloquea a los que ya estaban previamente. Hacer una función
que dada una lista con tuplas (<hora>,<entra/sale>,<invitado>,<espacio>) que están ordenadas por hora, indique
si la asignación de espacios es válida. Una asignación es inválida si algún invitado no puede salir a su horario
designado porque hay otro auto bloqueándole la salida.

Ejemplo: [(21,ENTRA,"Blas",2), (22,ENTRA,"Ailín",2), (23.5,SALE,"Blas",2), (24,SALE,"Ailín",2)] no es una asignación
válida porque el auto de Ailín no deja salir a Blas a horario. En cambio ésta sí es válida: [(21,ENTRA,"Blas",2),
(22,ENTRA,"Ailín",2), (23,SALE,"Ailín",2), (23.5,SALE,"Blas",2)].
"""
from pila import Pila

def posicion_vadida(lista):
    pila = Pila()
    for tupla in lista:
        if tupla[1] == "ENTRA":
            pila.apilar(tupla)
        else:
            if pila.ver_tope()[2] != tupla[2]:
                return False
            else:
                pila.desapilar()
    return True
print(posicion_vadida([(21, "ENTRA", "Blas", 2), (22, "ENTRA", "Ailín", 2), (23.5, "SALE", "Blas", 2), (24, "SALE", "Ailín", 2)]))
print(posicion_vadida([(21, "ENTRA", "Blas", 2), (22, "ENTRA", "Ailín", 2), (23, "SALE", "Ailín", 2), (23.5, "SALE", "Blas", 2)]))
print(posicion_vadida([(21, "ENTRA", "Blas", 2), (22, "ENTRA", "Ailín", 2), (23, "SALE", "Ailín", 2), (23.5, "SALE", "Blas", 2), (24, "ENTRA", "Ailín", 2), (25, "SALE", "Ailín", 2)]))