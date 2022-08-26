"""Escribir un programa que utilice la función anterior para generar una tabla de
conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10."""
def gradosAcelcius(valor):
    return((9/5)*valor+32)
def mostrarTabla():
    for i in range(0,120,10):
        convercion = gradosAcelcius(i)
        print(i, convercion)
        
mostrarTabla()