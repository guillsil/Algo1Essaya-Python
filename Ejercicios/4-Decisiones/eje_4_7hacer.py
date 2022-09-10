"""Escribir un programa que reciba como entrada un entero representando un
año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números
romanos."""
def romanos(n):
    # Muestra en pantalla el año en números romanos
    romanos = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    if n <= 1000:
        if n >= 100:
            if n >= 500:
                if n >= 900:
                    print("CM")
                else:
                    print("D", end="")
                    n = n - 500
            if n >= 400:
                print("CD")
            else:
                print("C" * (n // 100), end="")
                n = n % 100
        if n >= 10:
            if n >= 50:
                if n >= 90:
                    print("XC")
                else:
                    print("L", end="")
                    n = n - 50
            if n >= 40:
                print("XL")
            else:
                print("X" * (n // 10), end="")
                n = n % 10
        if n >= 1:
            if n >= 5:
                if n >= 9:
                    print("IX")
                else:
                    print("V", end="")
                    n = n - 5
            if n >= 4:
                print("IV")
            else:
                print("I" * n, end="")
                n = n % 1