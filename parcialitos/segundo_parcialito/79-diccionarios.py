""""Dado un diccionario cuyas claves son nombres de materias y sus valores son listas de enteros (que representan que dia 
del receso toman final), escribir una que devuelva un diccionario donde a cada fecha se le asigne una lista de materias
que toman final ese dia. 
Por ejemplo, d = {“Algoritmos 1”: [13,20], “Algoritmos 2”: [13,19]} dara como resultado 
{13: [““Algoritmos 1”, “Algoritmos 2”], 19: [““Algoritmos 2”], 20: [“Algoritmos 1”]}."""

def materias_por_fecha(d):
    diccionario = {}
    for materia in d:
        for fecha in d[materia]:
            if fecha not in diccionario:
                diccionario[fecha] = [materia]
            else:
                diccionario[fecha].append(materia)
    return diccionario
print(materias_por_fecha({"Algoritmos 1": [13,20], "Algoritmos 2": [13,19], "Algoritmos 3": [13,19], "Fisica 1": [14,20], "Fisica 2": [14,19]}))