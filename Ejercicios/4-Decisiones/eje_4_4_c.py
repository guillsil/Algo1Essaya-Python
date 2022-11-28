def interseccion(m1, b1, m2, b2):
    # Muestra en pantalla  el punto  intersección entre dos rectas en R2
    if m1 != m2 and m1%m2 != 0:
        print("La intersección es", "x = ",(b2 - b1) / (m1 - m2), ", y =", ((b2 - b1) / (m1 - m2)) * m1 + b1)
    else:
        print("Las rectas son paralelas")
print(interseccion(2, 1, 4, 3))