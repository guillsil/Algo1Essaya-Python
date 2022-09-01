"""Escribir dos funciones que permitan calcular:
a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
b) La duración en horas, minutos y segundos de un intervalo dado en segundos."""
def horaAsegundos(horas, minutos, segundos):
    return (horas*3600) + (minutos*60) + segundos
def segundosAhoras(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    return horas, minutos, segundos