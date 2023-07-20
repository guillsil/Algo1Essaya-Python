"""Escribir una función que reciba un número entero k e imprima su descomposición en factores primos.
Ejemplo:
>> descomposicion_factores_primos(25)
5
5
>> descomposicion_factores_primos(100)
2
2
5
5
>> descomposicion_factores_primos(57)
3
19
>> descomposicion_factores_primos(71)
71"""
def descomposicion_factores_primos(k):
    i = 2
    while i <= k:
        if k % i == 0:
            print(i)
            k = k // i
        else:
            i += 1

descomposicion_factores_primos(25)