"""Usando las funciones del ejercicio anterior, escribir un programa que pida al usua-
rio dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre
por pantalla la duración total en horas, minutos y segundos."""
from eje_3_1 import horaAsegundos, segundosAhoras
def main(hora1, minutos1, segundos1, hora2, minutos2, segundos2):
    segundosTotales = horaAsegundos(hora1, minutos1, segundos1) + horaAsegundos(hora2, minutos2, segundos2)
    print(segundosAhoras(segundosTotales))
main(1, 2, 3, 4, 5, 6)