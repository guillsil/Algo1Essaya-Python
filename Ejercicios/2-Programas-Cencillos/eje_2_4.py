"""Escribir un programa que utilice la función anterior para generar una tabla de
conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10."""
from eje_2_3 import gradosAcelcius

def main():
    for i in range(0,120,10):
        convercion = gradosAcelcius(i)
        print(i, convercion)
        
main()