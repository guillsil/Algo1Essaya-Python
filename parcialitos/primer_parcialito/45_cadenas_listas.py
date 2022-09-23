"""Escribir una función que, dada una lista de nombres y una letra, devuelva una lista con todos los nombres que
empiezan por dicha letra. La función debe ignorar mayúsculas y minúsculas; es decir, tanto "alan" como "Alan"
empiezan con "A" (y con "a")."""
def empiezaConLetra(nombres, letra):
    lista_nombres = []
    for nombre in nombres:
        if nombre[0].lower() == letra.lower():
            lista_nombres.append(nombre)
    return lista_nombres
print(empiezaConLetra(["alan", "Grace", "Hopper", "Bárbara", "Lovelace"], "a"))
