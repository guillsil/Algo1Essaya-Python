"""
a) Escribir una función que dado un número entero devuelva 1 si el mismo
es impar y 0 si fuera par.
b) Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si
fuera par.
c) Escribir una función que dado un número entero devuelva el dígito de las unidades. Por
ejemplo, para 153 debe devolver 3.
d) Escribir una función que dado un número devuelva el primer número múltiplo de 10
inferior a él. Por ejemplo, para 153 debe devolver 150."""
#a)
def fusion(num):
    #par
    if num%2==0:
        return 0
    #impar
    else:
        return 1
print(fusion(2))

#b)
def fusion(num):
    #par
    if num%2==0:
        return 1
    #impar
    else:
        return 0
print(fusion(2))

#c)
def digitoEnUnidades(num):
    print(len(str(num)))
digitoEnUnidades(200000)

#d)
def numMultiplo10(num):
    return num%10



