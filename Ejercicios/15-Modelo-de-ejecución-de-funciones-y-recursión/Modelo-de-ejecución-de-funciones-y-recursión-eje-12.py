"""Ya sabemos que la implementación recursiva del cálculo del número de Fibo-
nacci (𝐹𝑛 = 𝐹𝑛−1 + 𝐹𝑛−2, 𝐹0 = 0, 𝐹1 = 1) es ineficiente porque muchas de las ramas calculan
reiteradamente los mismos valores.
Escribir una función fibonacci(n) que calcule el enésimo número de Fibonacci de forma re-
cursiva pero que utilice un diccionario para almacenar los valores ya computados y no compu-
tarlos más de una vez.
Nota: Será necesario implementar una función wrapper para cumplir con la firma de la fun-
ción pedida."""
def fibonacci(n):
    '''
    Calcula el enésimo número de Fibonacci de forma recursiva pero que utilice un diccionario
    para almacenar los valores ya computados y no computarlos más de una vez.
    '''
    diccionario = {}
    def fibonacci_aux(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in diccionario:
                return diccionario[n]
            else:
                diccionario[n] = fibonacci_aux(n - 1) + fibonacci_aux(n - 2)
                return diccionario[n]
    return fibonacci_aux(n)
print(fibonacci(10))