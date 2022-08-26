"""Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
𝐶𝑛 = 𝐶 × (1 + 𝑥/100 )**𝑛
Donde 𝐶 es el capital inicial, 𝑥 es la tasa de interés y 𝑛 es el número de años a calcular.
"""
print("Ingrese el Capital Inicial")
capInicial = input()
print("Ingrese la tasa de interés")
tasaInteres = input()
print("Cual es el Número de Años")
numAños = input()
def monotributo(capInicial, tasaInteres, numAños):
    return (capInicial*(1+tasaInteres/100)**numAños)

print(monotributo(int(capInicial), int(tasaInteres), int(numAños)))